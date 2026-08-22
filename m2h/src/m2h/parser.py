# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

"""MSP430 assembly parser."""

import re
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional


class OperandType(Enum):
    """Addressing mode of an MSP430 operand."""

    REGISTER = auto()  # r4, sp, pc, etc.
    IMMEDIATE = auto()  # #123, #label
    INDIRECT = auto()  # @r4
    INDIRECT_AUTOINC = auto()  # @r4+
    INDEXED = auto()  # 4(r1), -2(r4), label(r5)
    ABSOLUTE = auto()  # &var, symbol


@dataclass
class Operand:
    """Represents a parsed operand."""

    op_type: OperandType
    value: str
    reg: Optional[str] = None  # Register used in INDEXED mode

    def __str__(self) -> str:
        if self.op_type == OperandType.REGISTER:
            return self.value
        elif self.op_type == OperandType.IMMEDIATE:
            return f"#{self.value}"
        elif self.op_type == OperandType.INDIRECT:
            return f"@{self.value}"
        elif self.op_type == OperandType.INDIRECT_AUTOINC:
            return f"@{self.value}+"
        elif self.op_type == OperandType.INDEXED:
            return f"{self.value}({self.reg})"
        elif self.op_type == OperandType.ABSOLUTE:
            return self.value
        return self.value


@dataclass
class Statement:
    """Represents a parsed assembly statement (label, instruction, or directive)."""

    line_number: int
    raw_line: str
    label: Optional[str] = None
    mnemonic: Optional[str] = None
    operands: list[Operand] = field(default_factory=list)
    directive: Optional[str] = None
    directive_args: list[str] = field(default_factory=list)


def normalize_register_name(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def is_register(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(re.match(r"^r(1[0-5]|[0-9])$", normalized))


def parse_operand(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(op_type=OperandType.IMMEDIATE, value=val)

    # Indirect Autoincrement: @r4+
    if s.startswith("@") and s.endswith("+"):
        reg_name = normalize_register_name(s[1:-1])
        if is_register(reg_name):
            return Operand(op_type=OperandType.INDIRECT_AUTOINC, value=reg_name)
        raise ValueError(f"Invalid register in autoincrement operand: '{s}'")

    # Indirect: @r4
    if s.startswith("@"):
        reg_name = normalize_register_name(s[1:])
        if is_register(reg_name):
            return Operand(op_type=OperandType.INDIRECT, value=reg_name)
        raise ValueError(f"Invalid register in indirect operand: '{s}'")

    # Indexed: offset(reg), e.g., 4(r1), -2(r4), label(r5)
    indexed_match = re.match(r"^([^(]+)\(([^)]+)\)$", s)
    if indexed_match:
        offset = indexed_match.group(1).strip()
        reg_name = normalize_register_name(indexed_match.group(2))
        if is_register(reg_name):
            return Operand(op_type=OperandType.INDEXED, value=offset, reg=reg_name)
        raise ValueError(f"Invalid register in indexed operand: '{s}'")

    # Absolute / Symbolic: &var
    if s.startswith("&"):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def clean_line(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def parse_line(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = cleaned

    # Check for label (e.g. main: or .L2:)
    # Label is identifier at the start followed by ':'
    label_match = re.match(r"^([a-zA-Z0-9_$.]+):\s*(.*)$", current)
    if label_match:
        stmt.label = label_match.group(1)
        current = label_match.group(2).strip()
        if not current:
            return stmt

    # Check for directive (e.g. .globl, .word, .comm)
    if current.startswith("."):
        parts = current.split(None, 1)
        stmt.directive = parts[0]
        if len(parts) > 1:
            # Parse comma-separated directive arguments
            stmt.directive_args = [arg.strip() for arg in parts[1].split(",")]
        return stmt

    # Instruction: mnemonic [operands]
    parts = current.split(None, 1)
    mnemonic_raw = parts[0]
    # Normalize mnemonic (strip .w or .b if present, case-insensitive)
    mnemonic_lower = mnemonic_raw.lower()
    if mnemonic_lower.endswith(".w") or mnemonic_lower.endswith(".b"):
        stmt.mnemonic = mnemonic_lower[:-2]
    else:
        stmt.mnemonic = mnemonic_lower

    if len(parts) > 1:
        # Split operands by comma (taking care not to split inside parentheses)
        operand_strs = []
        depth = 0
        current_op = []
        for char in parts[1]:
            if char == "(":
                depth += 1
                current_op.append(char)
            elif char == ")":
                depth -= 1
                current_op.append(char)
            elif char == "," and depth == 0:
                operand_strs.append("".join(current_op).strip())
                current_op = []
            else:
                current_op.append(char)
        if current_op:
            operand_strs.append("".join(current_op).strip())

        for op_str in operand_strs:
            if op_str:
                stmt.operands.append(parse_operand(op_str))

    return stmt


def parse_assembly(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements
