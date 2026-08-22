# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

"""MSP430 assembly parser."""

import re
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_x_normalize_register_name__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_normalize_register_name__mutmut)
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


def x_normalize_register_name__mutmut_orig(name: str) -> str:
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


def x_normalize_register_name__mutmut_1(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = None
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_2(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().upper()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_3(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg != "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_4(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "XXspXX":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_5(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "SP":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_6(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "XXr1XX"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_7(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "R1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_8(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg != "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_9(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "XXpcXX":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_10(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "PC":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_11(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "XXr0XX"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_12(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "R0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_13(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg != "sr":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_14(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "XXsrXX":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_15(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "SR":
        return "r2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_16(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "XXr2XX"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_17(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "R2"
    if reg == "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_18(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg != "cg":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_19(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "XXcgXX":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_20(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "CG":
        return "r3"
    return reg


def x_normalize_register_name__mutmut_21(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "XXr3XX"
    return reg


def x_normalize_register_name__mutmut_22(name: str) -> str:
    """Normalize register aliases (sp, pc, sr) to canonical lowercase form."""
    reg = name.strip().lower()
    if reg == "sp":
        return "r1"
    if reg == "pc":
        return "r0"
    if reg == "sr":
        return "r2"
    if reg == "cg":
        return "R3"
    return reg

mutants_x_normalize_register_name__mutmut['_mutmut_orig'] = x_normalize_register_name__mutmut_orig # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_1'] = x_normalize_register_name__mutmut_1 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_2'] = x_normalize_register_name__mutmut_2 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_3'] = x_normalize_register_name__mutmut_3 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_4'] = x_normalize_register_name__mutmut_4 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_5'] = x_normalize_register_name__mutmut_5 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_6'] = x_normalize_register_name__mutmut_6 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_7'] = x_normalize_register_name__mutmut_7 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_8'] = x_normalize_register_name__mutmut_8 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_9'] = x_normalize_register_name__mutmut_9 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_10'] = x_normalize_register_name__mutmut_10 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_11'] = x_normalize_register_name__mutmut_11 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_12'] = x_normalize_register_name__mutmut_12 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_13'] = x_normalize_register_name__mutmut_13 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_14'] = x_normalize_register_name__mutmut_14 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_15'] = x_normalize_register_name__mutmut_15 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_16'] = x_normalize_register_name__mutmut_16 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_17'] = x_normalize_register_name__mutmut_17 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_18'] = x_normalize_register_name__mutmut_18 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_19'] = x_normalize_register_name__mutmut_19 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_20'] = x_normalize_register_name__mutmut_20 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_21'] = x_normalize_register_name__mutmut_21 # type: ignore # mutmut generated
mutants_x_normalize_register_name__mutmut['x_normalize_register_name__mutmut_22'] = x_normalize_register_name__mutmut_22 # type: ignore # mutmut generated
mutants_x_is_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_register__mutmut)
def is_register(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(re.match(r"^r(1[0-5]|[0-9])$", normalized))


def x_is_register__mutmut_orig(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(re.match(r"^r(1[0-5]|[0-9])$", normalized))


def x_is_register__mutmut_1(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = None
    return bool(re.match(r"^r(1[0-5]|[0-9])$", normalized))


def x_is_register__mutmut_2(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(None)
    return bool(re.match(r"^r(1[0-5]|[0-9])$", normalized))


def x_is_register__mutmut_3(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(None)


def x_is_register__mutmut_4(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(re.match(None, normalized))


def x_is_register__mutmut_5(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(re.match(r"^r(1[0-5]|[0-9])$", None))


def x_is_register__mutmut_6(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(re.match(normalized))


def x_is_register__mutmut_7(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(re.match(r"^r(1[0-5]|[0-9])$", ))


def x_is_register__mutmut_8(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(re.match(r"XX^r(1[0-5]|[0-9])$XX", normalized))


def x_is_register__mutmut_9(name: str) -> bool:
    """Check if the name is an MSP430 register (r0..r15, sp, pc, sr, cg)."""
    normalized = normalize_register_name(name)
    return bool(re.match(r"^R(1[0-5]|[0-9])$", normalized))

mutants_x_is_register__mutmut['_mutmut_orig'] = x_is_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_register__mutmut['x_is_register__mutmut_1'] = x_is_register__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_register__mutmut['x_is_register__mutmut_2'] = x_is_register__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_register__mutmut['x_is_register__mutmut_3'] = x_is_register__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_register__mutmut['x_is_register__mutmut_4'] = x_is_register__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_register__mutmut['x_is_register__mutmut_5'] = x_is_register__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_register__mutmut['x_is_register__mutmut_6'] = x_is_register__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_register__mutmut['x_is_register__mutmut_7'] = x_is_register__mutmut_7 # type: ignore # mutmut generated
mutants_x_is_register__mutmut['x_is_register__mutmut_8'] = x_is_register__mutmut_8 # type: ignore # mutmut generated
mutants_x_is_register__mutmut['x_is_register__mutmut_9'] = x_is_register__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_operand__mutmut)
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


def x_parse_operand__mutmut_orig(op_str: str) -> Operand:
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


def x_parse_operand__mutmut_1(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = None
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


def x_parse_operand__mutmut_2(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if s:
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


def x_parse_operand__mutmut_3(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError(None)

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


def x_parse_operand__mutmut_4(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("XXEmpty operand stringXX")

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


def x_parse_operand__mutmut_5(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("empty operand string")

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


def x_parse_operand__mutmut_6(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("EMPTY OPERAND STRING")

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


def x_parse_operand__mutmut_7(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith(None):
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


def x_parse_operand__mutmut_8(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("XX#XX"):
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


def x_parse_operand__mutmut_9(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = None
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


def x_parse_operand__mutmut_10(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[2:].strip()
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


def x_parse_operand__mutmut_11(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(op_type=None, value=val)

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


def x_parse_operand__mutmut_12(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(op_type=OperandType.IMMEDIATE, value=None)

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


def x_parse_operand__mutmut_13(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(value=val)

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


def x_parse_operand__mutmut_14(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(op_type=OperandType.IMMEDIATE, )

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


def x_parse_operand__mutmut_15(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(op_type=OperandType.IMMEDIATE, value=val)

    # Indirect Autoincrement: @r4+
    if s.startswith("@") or s.endswith("+"):
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


def x_parse_operand__mutmut_16(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(op_type=OperandType.IMMEDIATE, value=val)

    # Indirect Autoincrement: @r4+
    if s.startswith(None) and s.endswith("+"):
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


def x_parse_operand__mutmut_17(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(op_type=OperandType.IMMEDIATE, value=val)

    # Indirect Autoincrement: @r4+
    if s.startswith("XX@XX") and s.endswith("+"):
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


def x_parse_operand__mutmut_18(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(op_type=OperandType.IMMEDIATE, value=val)

    # Indirect Autoincrement: @r4+
    if s.startswith("@") and s.endswith(None):
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


def x_parse_operand__mutmut_19(op_str: str) -> Operand:
    """Parse an operand string into an Operand object."""
    s = op_str.strip()
    if not s:
        raise ValueError("Empty operand string")

    # Immediate: #123, #symbol, #-4
    if s.startswith("#"):
        val = s[1:].strip()
        return Operand(op_type=OperandType.IMMEDIATE, value=val)

    # Indirect Autoincrement: @r4+
    if s.startswith("@") and s.endswith("XX+XX"):
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


def x_parse_operand__mutmut_20(op_str: str) -> Operand:
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
        reg_name = None
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


def x_parse_operand__mutmut_21(op_str: str) -> Operand:
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
        reg_name = normalize_register_name(None)
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


def x_parse_operand__mutmut_22(op_str: str) -> Operand:
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
        reg_name = normalize_register_name(s[2:-1])
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


def x_parse_operand__mutmut_23(op_str: str) -> Operand:
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
        reg_name = normalize_register_name(s[1:+1])
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


def x_parse_operand__mutmut_24(op_str: str) -> Operand:
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
        reg_name = normalize_register_name(s[1:-2])
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


def x_parse_operand__mutmut_25(op_str: str) -> Operand:
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
        if is_register(None):
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


def x_parse_operand__mutmut_26(op_str: str) -> Operand:
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
            return Operand(op_type=None, value=reg_name)
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


def x_parse_operand__mutmut_27(op_str: str) -> Operand:
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
            return Operand(op_type=OperandType.INDIRECT_AUTOINC, value=None)
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


def x_parse_operand__mutmut_28(op_str: str) -> Operand:
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
            return Operand(value=reg_name)
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


def x_parse_operand__mutmut_29(op_str: str) -> Operand:
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
            return Operand(op_type=OperandType.INDIRECT_AUTOINC, )
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


def x_parse_operand__mutmut_30(op_str: str) -> Operand:
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
        raise ValueError(None)

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


def x_parse_operand__mutmut_31(op_str: str) -> Operand:
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
    if s.startswith(None):
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


def x_parse_operand__mutmut_32(op_str: str) -> Operand:
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
    if s.startswith("XX@XX"):
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


def x_parse_operand__mutmut_33(op_str: str) -> Operand:
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
        reg_name = None
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


def x_parse_operand__mutmut_34(op_str: str) -> Operand:
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
        reg_name = normalize_register_name(None)
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


def x_parse_operand__mutmut_35(op_str: str) -> Operand:
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
        reg_name = normalize_register_name(s[2:])
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


def x_parse_operand__mutmut_36(op_str: str) -> Operand:
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
        if is_register(None):
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


def x_parse_operand__mutmut_37(op_str: str) -> Operand:
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
            return Operand(op_type=None, value=reg_name)
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


def x_parse_operand__mutmut_38(op_str: str) -> Operand:
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
            return Operand(op_type=OperandType.INDIRECT, value=None)
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


def x_parse_operand__mutmut_39(op_str: str) -> Operand:
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
            return Operand(value=reg_name)
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


def x_parse_operand__mutmut_40(op_str: str) -> Operand:
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
            return Operand(op_type=OperandType.INDIRECT, )
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


def x_parse_operand__mutmut_41(op_str: str) -> Operand:
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
        raise ValueError(None)

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


def x_parse_operand__mutmut_42(op_str: str) -> Operand:
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
    indexed_match = None
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


def x_parse_operand__mutmut_43(op_str: str) -> Operand:
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
    indexed_match = re.match(None, s)
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


def x_parse_operand__mutmut_44(op_str: str) -> Operand:
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
    indexed_match = re.match(r"^([^(]+)\(([^)]+)\)$", None)
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


def x_parse_operand__mutmut_45(op_str: str) -> Operand:
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
    indexed_match = re.match(s)
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


def x_parse_operand__mutmut_46(op_str: str) -> Operand:
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
    indexed_match = re.match(r"^([^(]+)\(([^)]+)\)$", )
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


def x_parse_operand__mutmut_47(op_str: str) -> Operand:
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
    indexed_match = re.match(r"XX^([^(]+)\(([^)]+)\)$XX", s)
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


def x_parse_operand__mutmut_48(op_str: str) -> Operand:
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
        offset = None
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


def x_parse_operand__mutmut_49(op_str: str) -> Operand:
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
        offset = indexed_match.group(None).strip()
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


def x_parse_operand__mutmut_50(op_str: str) -> Operand:
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
        offset = indexed_match.group(2).strip()
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


def x_parse_operand__mutmut_51(op_str: str) -> Operand:
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
        reg_name = None
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


def x_parse_operand__mutmut_52(op_str: str) -> Operand:
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
        reg_name = normalize_register_name(None)
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


def x_parse_operand__mutmut_53(op_str: str) -> Operand:
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
        reg_name = normalize_register_name(indexed_match.group(None))
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


def x_parse_operand__mutmut_54(op_str: str) -> Operand:
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
        reg_name = normalize_register_name(indexed_match.group(3))
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


def x_parse_operand__mutmut_55(op_str: str) -> Operand:
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
        if is_register(None):
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


def x_parse_operand__mutmut_56(op_str: str) -> Operand:
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
            return Operand(op_type=None, value=offset, reg=reg_name)
        raise ValueError(f"Invalid register in indexed operand: '{s}'")

    # Absolute / Symbolic: &var
    if s.startswith("&"):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_57(op_str: str) -> Operand:
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
            return Operand(op_type=OperandType.INDEXED, value=None, reg=reg_name)
        raise ValueError(f"Invalid register in indexed operand: '{s}'")

    # Absolute / Symbolic: &var
    if s.startswith("&"):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_58(op_str: str) -> Operand:
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
            return Operand(op_type=OperandType.INDEXED, value=offset, reg=None)
        raise ValueError(f"Invalid register in indexed operand: '{s}'")

    # Absolute / Symbolic: &var
    if s.startswith("&"):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_59(op_str: str) -> Operand:
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
            return Operand(value=offset, reg=reg_name)
        raise ValueError(f"Invalid register in indexed operand: '{s}'")

    # Absolute / Symbolic: &var
    if s.startswith("&"):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_60(op_str: str) -> Operand:
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
            return Operand(op_type=OperandType.INDEXED, reg=reg_name)
        raise ValueError(f"Invalid register in indexed operand: '{s}'")

    # Absolute / Symbolic: &var
    if s.startswith("&"):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_61(op_str: str) -> Operand:
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
            return Operand(op_type=OperandType.INDEXED, value=offset, )
        raise ValueError(f"Invalid register in indexed operand: '{s}'")

    # Absolute / Symbolic: &var
    if s.startswith("&"):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_62(op_str: str) -> Operand:
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
        raise ValueError(None)

    # Absolute / Symbolic: &var
    if s.startswith("&"):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_63(op_str: str) -> Operand:
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
    if s.startswith(None):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_64(op_str: str) -> Operand:
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
    if s.startswith("XX&XX"):
        return Operand(op_type=OperandType.ABSOLUTE, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_65(op_str: str) -> Operand:
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
        return Operand(op_type=None, value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_66(op_str: str) -> Operand:
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
        return Operand(op_type=OperandType.ABSOLUTE, value=None)

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_67(op_str: str) -> Operand:
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
        return Operand(value=s[1:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_68(op_str: str) -> Operand:
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
        return Operand(op_type=OperandType.ABSOLUTE, )

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_69(op_str: str) -> Operand:
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
        return Operand(op_type=OperandType.ABSOLUTE, value=s[2:].strip())

    # Register: r0..r15, sp, pc
    if is_register(s):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_70(op_str: str) -> Operand:
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
    if is_register(None):
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_71(op_str: str) -> Operand:
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
        return Operand(op_type=None, value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_72(op_str: str) -> Operand:
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
        return Operand(op_type=OperandType.REGISTER, value=None)

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_73(op_str: str) -> Operand:
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
        return Operand(value=normalize_register_name(s))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_74(op_str: str) -> Operand:
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
        return Operand(op_type=OperandType.REGISTER, )

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_75(op_str: str) -> Operand:
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
        return Operand(op_type=OperandType.REGISTER, value=normalize_register_name(None))

    # Absolute symbol or address
    return Operand(op_type=OperandType.ABSOLUTE, value=s)


def x_parse_operand__mutmut_76(op_str: str) -> Operand:
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
    return Operand(op_type=None, value=s)


def x_parse_operand__mutmut_77(op_str: str) -> Operand:
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
    return Operand(op_type=OperandType.ABSOLUTE, value=None)


def x_parse_operand__mutmut_78(op_str: str) -> Operand:
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
    return Operand(value=s)


def x_parse_operand__mutmut_79(op_str: str) -> Operand:
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
    return Operand(op_type=OperandType.ABSOLUTE, )

mutants_x_parse_operand__mutmut['_mutmut_orig'] = x_parse_operand__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_1'] = x_parse_operand__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_2'] = x_parse_operand__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_3'] = x_parse_operand__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_4'] = x_parse_operand__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_5'] = x_parse_operand__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_6'] = x_parse_operand__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_7'] = x_parse_operand__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_8'] = x_parse_operand__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_9'] = x_parse_operand__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_10'] = x_parse_operand__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_11'] = x_parse_operand__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_12'] = x_parse_operand__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_13'] = x_parse_operand__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_14'] = x_parse_operand__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_15'] = x_parse_operand__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_16'] = x_parse_operand__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_17'] = x_parse_operand__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_18'] = x_parse_operand__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_19'] = x_parse_operand__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_20'] = x_parse_operand__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_21'] = x_parse_operand__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_22'] = x_parse_operand__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_23'] = x_parse_operand__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_24'] = x_parse_operand__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_25'] = x_parse_operand__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_26'] = x_parse_operand__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_27'] = x_parse_operand__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_28'] = x_parse_operand__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_29'] = x_parse_operand__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_30'] = x_parse_operand__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_31'] = x_parse_operand__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_32'] = x_parse_operand__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_33'] = x_parse_operand__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_34'] = x_parse_operand__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_35'] = x_parse_operand__mutmut_35 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_36'] = x_parse_operand__mutmut_36 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_37'] = x_parse_operand__mutmut_37 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_38'] = x_parse_operand__mutmut_38 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_39'] = x_parse_operand__mutmut_39 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_40'] = x_parse_operand__mutmut_40 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_41'] = x_parse_operand__mutmut_41 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_42'] = x_parse_operand__mutmut_42 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_43'] = x_parse_operand__mutmut_43 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_44'] = x_parse_operand__mutmut_44 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_45'] = x_parse_operand__mutmut_45 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_46'] = x_parse_operand__mutmut_46 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_47'] = x_parse_operand__mutmut_47 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_48'] = x_parse_operand__mutmut_48 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_49'] = x_parse_operand__mutmut_49 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_50'] = x_parse_operand__mutmut_50 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_51'] = x_parse_operand__mutmut_51 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_52'] = x_parse_operand__mutmut_52 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_53'] = x_parse_operand__mutmut_53 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_54'] = x_parse_operand__mutmut_54 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_55'] = x_parse_operand__mutmut_55 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_56'] = x_parse_operand__mutmut_56 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_57'] = x_parse_operand__mutmut_57 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_58'] = x_parse_operand__mutmut_58 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_59'] = x_parse_operand__mutmut_59 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_60'] = x_parse_operand__mutmut_60 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_61'] = x_parse_operand__mutmut_61 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_62'] = x_parse_operand__mutmut_62 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_63'] = x_parse_operand__mutmut_63 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_64'] = x_parse_operand__mutmut_64 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_65'] = x_parse_operand__mutmut_65 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_66'] = x_parse_operand__mutmut_66 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_67'] = x_parse_operand__mutmut_67 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_68'] = x_parse_operand__mutmut_68 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_69'] = x_parse_operand__mutmut_69 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_70'] = x_parse_operand__mutmut_70 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_71'] = x_parse_operand__mutmut_71 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_72'] = x_parse_operand__mutmut_72 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_73'] = x_parse_operand__mutmut_73 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_74'] = x_parse_operand__mutmut_74 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_75'] = x_parse_operand__mutmut_75 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_76'] = x_parse_operand__mutmut_76 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_77'] = x_parse_operand__mutmut_77 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_78'] = x_parse_operand__mutmut_78 # type: ignore # mutmut generated
mutants_x_parse_operand__mutmut['x_parse_operand__mutmut_79'] = x_parse_operand__mutmut_79 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_clean_line__mutmut)
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


def x_clean_line__mutmut_orig(line: str) -> str:
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


def x_clean_line__mutmut_1(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = None
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_2(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = +1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_3(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -2
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_4(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in ["XX;XX", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_5(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "XX//XX"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_6(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = None
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_7(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(None)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_8(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.rfind(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_9(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 or (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_10(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p == -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_11(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != +1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_12(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -2 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_13(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 and p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_14(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos != -1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_15(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == +1 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_16(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -2 or p < pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_17(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p <= pos):
            pos = p
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_18(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = None
    if pos != -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_19(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos == -1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_20(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != +1:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_21(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -2:
        line = line[:pos]
    return line.strip()


def x_clean_line__mutmut_22(line: str) -> str:
    """Strip comments and surrounding whitespace."""
    # Remove ; or // comments
    pos = -1
    for comment_marker in [";", "//"]:
        p = line.find(comment_marker)
        if p != -1 and (pos == -1 or p < pos):
            pos = p
    if pos != -1:
        line = None
    return line.strip()

mutants_x_clean_line__mutmut['_mutmut_orig'] = x_clean_line__mutmut_orig # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_1'] = x_clean_line__mutmut_1 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_2'] = x_clean_line__mutmut_2 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_3'] = x_clean_line__mutmut_3 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_4'] = x_clean_line__mutmut_4 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_5'] = x_clean_line__mutmut_5 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_6'] = x_clean_line__mutmut_6 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_7'] = x_clean_line__mutmut_7 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_8'] = x_clean_line__mutmut_8 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_9'] = x_clean_line__mutmut_9 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_10'] = x_clean_line__mutmut_10 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_11'] = x_clean_line__mutmut_11 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_12'] = x_clean_line__mutmut_12 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_13'] = x_clean_line__mutmut_13 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_14'] = x_clean_line__mutmut_14 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_15'] = x_clean_line__mutmut_15 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_16'] = x_clean_line__mutmut_16 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_17'] = x_clean_line__mutmut_17 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_18'] = x_clean_line__mutmut_18 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_19'] = x_clean_line__mutmut_19 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_20'] = x_clean_line__mutmut_20 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_21'] = x_clean_line__mutmut_21 # type: ignore # mutmut generated
mutants_x_clean_line__mutmut['x_clean_line__mutmut_22'] = x_clean_line__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_line__mutmut)
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


def x_parse_line__mutmut_orig(line: str, line_number: int = 0) -> Optional[Statement]:
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


def x_parse_line__mutmut_1(line: str, line_number: int = 1) -> Optional[Statement]:
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


def x_parse_line__mutmut_2(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = None
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


def x_parse_line__mutmut_3(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(None)
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


def x_parse_line__mutmut_4(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if cleaned:
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


def x_parse_line__mutmut_5(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = None
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


def x_parse_line__mutmut_6(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=None, raw_line=line)
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


def x_parse_line__mutmut_7(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=None)
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


def x_parse_line__mutmut_8(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(raw_line=line)
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


def x_parse_line__mutmut_9(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, )
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


def x_parse_line__mutmut_10(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = None

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


def x_parse_line__mutmut_11(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = cleaned

    # Check for label (e.g. main: or .L2:)
    # Label is identifier at the start followed by ':'
    label_match = None
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


def x_parse_line__mutmut_12(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = cleaned

    # Check for label (e.g. main: or .L2:)
    # Label is identifier at the start followed by ':'
    label_match = re.match(None, current)
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


def x_parse_line__mutmut_13(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = cleaned

    # Check for label (e.g. main: or .L2:)
    # Label is identifier at the start followed by ':'
    label_match = re.match(r"^([a-zA-Z0-9_$.]+):\s*(.*)$", None)
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


def x_parse_line__mutmut_14(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = cleaned

    # Check for label (e.g. main: or .L2:)
    # Label is identifier at the start followed by ':'
    label_match = re.match(current)
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


def x_parse_line__mutmut_15(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = cleaned

    # Check for label (e.g. main: or .L2:)
    # Label is identifier at the start followed by ':'
    label_match = re.match(r"^([a-zA-Z0-9_$.]+):\s*(.*)$", )
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


def x_parse_line__mutmut_16(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = cleaned

    # Check for label (e.g. main: or .L2:)
    # Label is identifier at the start followed by ':'
    label_match = re.match(r"XX^([a-zA-Z0-9_$.]+):\s*(.*)$XX", current)
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


def x_parse_line__mutmut_17(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = cleaned

    # Check for label (e.g. main: or .L2:)
    # Label is identifier at the start followed by ':'
    label_match = re.match(r"^([a-za-z0-9_$.]+):\s*(.*)$", current)
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


def x_parse_line__mutmut_18(line: str, line_number: int = 0) -> Optional[Statement]:
    """Parse a single line of MSP430 assembly."""
    cleaned = clean_line(line)
    if not cleaned:
        return None

    stmt = Statement(line_number=line_number, raw_line=line)
    current = cleaned

    # Check for label (e.g. main: or .L2:)
    # Label is identifier at the start followed by ':'
    label_match = re.match(r"^([A-ZA-Z0-9_$.]+):\s*(.*)$", current)
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


def x_parse_line__mutmut_19(line: str, line_number: int = 0) -> Optional[Statement]:
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
        stmt.label = None
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


def x_parse_line__mutmut_20(line: str, line_number: int = 0) -> Optional[Statement]:
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
        stmt.label = label_match.group(None)
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


def x_parse_line__mutmut_21(line: str, line_number: int = 0) -> Optional[Statement]:
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
        stmt.label = label_match.group(2)
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


def x_parse_line__mutmut_22(line: str, line_number: int = 0) -> Optional[Statement]:
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
        current = None
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


def x_parse_line__mutmut_23(line: str, line_number: int = 0) -> Optional[Statement]:
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
        current = label_match.group(None).strip()
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


def x_parse_line__mutmut_24(line: str, line_number: int = 0) -> Optional[Statement]:
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
        current = label_match.group(3).strip()
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


def x_parse_line__mutmut_25(line: str, line_number: int = 0) -> Optional[Statement]:
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
        if current:
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


def x_parse_line__mutmut_26(line: str, line_number: int = 0) -> Optional[Statement]:
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
    if current.startswith(None):
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


def x_parse_line__mutmut_27(line: str, line_number: int = 0) -> Optional[Statement]:
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
    if current.startswith("XX.XX"):
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


def x_parse_line__mutmut_28(line: str, line_number: int = 0) -> Optional[Statement]:
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
        parts = None
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


def x_parse_line__mutmut_29(line: str, line_number: int = 0) -> Optional[Statement]:
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
        parts = current.split(None, None)
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


def x_parse_line__mutmut_30(line: str, line_number: int = 0) -> Optional[Statement]:
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
        parts = current.split(1)
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


def x_parse_line__mutmut_31(line: str, line_number: int = 0) -> Optional[Statement]:
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
        parts = current.split(None, )
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


def x_parse_line__mutmut_32(line: str, line_number: int = 0) -> Optional[Statement]:
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
        parts = current.rsplit(None, 1)
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


def x_parse_line__mutmut_33(line: str, line_number: int = 0) -> Optional[Statement]:
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
        parts = current.split(None, 2)
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


def x_parse_line__mutmut_34(line: str, line_number: int = 0) -> Optional[Statement]:
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
        stmt.directive = None
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


def x_parse_line__mutmut_35(line: str, line_number: int = 0) -> Optional[Statement]:
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
        stmt.directive = parts[1]
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


def x_parse_line__mutmut_36(line: str, line_number: int = 0) -> Optional[Statement]:
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
        if len(parts) >= 1:
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


def x_parse_line__mutmut_37(line: str, line_number: int = 0) -> Optional[Statement]:
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
        if len(parts) > 2:
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


def x_parse_line__mutmut_38(line: str, line_number: int = 0) -> Optional[Statement]:
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
            stmt.directive_args = None
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


def x_parse_line__mutmut_39(line: str, line_number: int = 0) -> Optional[Statement]:
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
            stmt.directive_args = [arg.strip() for arg in parts[1].split(None)]
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


def x_parse_line__mutmut_40(line: str, line_number: int = 0) -> Optional[Statement]:
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
            stmt.directive_args = [arg.strip() for arg in parts[2].split(",")]
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


def x_parse_line__mutmut_41(line: str, line_number: int = 0) -> Optional[Statement]:
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
            stmt.directive_args = [arg.strip() for arg in parts[1].split("XX,XX")]
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


def x_parse_line__mutmut_42(line: str, line_number: int = 0) -> Optional[Statement]:
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
    parts = None
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


def x_parse_line__mutmut_43(line: str, line_number: int = 0) -> Optional[Statement]:
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
    parts = current.split(None, None)
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


def x_parse_line__mutmut_44(line: str, line_number: int = 0) -> Optional[Statement]:
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
    parts = current.split(1)
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


def x_parse_line__mutmut_45(line: str, line_number: int = 0) -> Optional[Statement]:
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
    parts = current.split(None, )
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


def x_parse_line__mutmut_46(line: str, line_number: int = 0) -> Optional[Statement]:
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
    parts = current.rsplit(None, 1)
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


def x_parse_line__mutmut_47(line: str, line_number: int = 0) -> Optional[Statement]:
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
    parts = current.split(None, 2)
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


def x_parse_line__mutmut_48(line: str, line_number: int = 0) -> Optional[Statement]:
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
    mnemonic_raw = None
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


def x_parse_line__mutmut_49(line: str, line_number: int = 0) -> Optional[Statement]:
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
    mnemonic_raw = parts[1]
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


def x_parse_line__mutmut_50(line: str, line_number: int = 0) -> Optional[Statement]:
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
    mnemonic_lower = None
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


def x_parse_line__mutmut_51(line: str, line_number: int = 0) -> Optional[Statement]:
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
    mnemonic_lower = mnemonic_raw.upper()
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


def x_parse_line__mutmut_52(line: str, line_number: int = 0) -> Optional[Statement]:
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
    if mnemonic_lower.endswith(".w") and mnemonic_lower.endswith(".b"):
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


def x_parse_line__mutmut_53(line: str, line_number: int = 0) -> Optional[Statement]:
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
    if mnemonic_lower.endswith(None) or mnemonic_lower.endswith(".b"):
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


def x_parse_line__mutmut_54(line: str, line_number: int = 0) -> Optional[Statement]:
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
    if mnemonic_lower.endswith("XX.wXX") or mnemonic_lower.endswith(".b"):
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


def x_parse_line__mutmut_55(line: str, line_number: int = 0) -> Optional[Statement]:
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
    if mnemonic_lower.endswith(".W") or mnemonic_lower.endswith(".b"):
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


def x_parse_line__mutmut_56(line: str, line_number: int = 0) -> Optional[Statement]:
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
    if mnemonic_lower.endswith(".w") or mnemonic_lower.endswith(None):
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


def x_parse_line__mutmut_57(line: str, line_number: int = 0) -> Optional[Statement]:
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
    if mnemonic_lower.endswith(".w") or mnemonic_lower.endswith("XX.bXX"):
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


def x_parse_line__mutmut_58(line: str, line_number: int = 0) -> Optional[Statement]:
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
    if mnemonic_lower.endswith(".w") or mnemonic_lower.endswith(".B"):
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


def x_parse_line__mutmut_59(line: str, line_number: int = 0) -> Optional[Statement]:
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
        stmt.mnemonic = None
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


def x_parse_line__mutmut_60(line: str, line_number: int = 0) -> Optional[Statement]:
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
        stmt.mnemonic = mnemonic_lower[:+2]
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


def x_parse_line__mutmut_61(line: str, line_number: int = 0) -> Optional[Statement]:
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
        stmt.mnemonic = mnemonic_lower[:-3]
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


def x_parse_line__mutmut_62(line: str, line_number: int = 0) -> Optional[Statement]:
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
        stmt.mnemonic = None

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


def x_parse_line__mutmut_63(line: str, line_number: int = 0) -> Optional[Statement]:
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

    if len(parts) >= 1:
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


def x_parse_line__mutmut_64(line: str, line_number: int = 0) -> Optional[Statement]:
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

    if len(parts) > 2:
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


def x_parse_line__mutmut_65(line: str, line_number: int = 0) -> Optional[Statement]:
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
        operand_strs = None
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


def x_parse_line__mutmut_66(line: str, line_number: int = 0) -> Optional[Statement]:
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
        depth = None
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


def x_parse_line__mutmut_67(line: str, line_number: int = 0) -> Optional[Statement]:
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
        depth = 1
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


def x_parse_line__mutmut_68(line: str, line_number: int = 0) -> Optional[Statement]:
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
        current_op = None
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


def x_parse_line__mutmut_69(line: str, line_number: int = 0) -> Optional[Statement]:
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
        for char in parts[2]:
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


def x_parse_line__mutmut_70(line: str, line_number: int = 0) -> Optional[Statement]:
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
            if char != "(":
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


def x_parse_line__mutmut_71(line: str, line_number: int = 0) -> Optional[Statement]:
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
            if char == "XX(XX":
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


def x_parse_line__mutmut_72(line: str, line_number: int = 0) -> Optional[Statement]:
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
                depth = 1
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


def x_parse_line__mutmut_73(line: str, line_number: int = 0) -> Optional[Statement]:
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
                depth -= 1
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


def x_parse_line__mutmut_74(line: str, line_number: int = 0) -> Optional[Statement]:
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
                depth += 2
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


def x_parse_line__mutmut_75(line: str, line_number: int = 0) -> Optional[Statement]:
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
                current_op.append(None)
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


def x_parse_line__mutmut_76(line: str, line_number: int = 0) -> Optional[Statement]:
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
            elif char != ")":
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


def x_parse_line__mutmut_77(line: str, line_number: int = 0) -> Optional[Statement]:
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
            elif char == "XX)XX":
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


def x_parse_line__mutmut_78(line: str, line_number: int = 0) -> Optional[Statement]:
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
                depth = 1
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


def x_parse_line__mutmut_79(line: str, line_number: int = 0) -> Optional[Statement]:
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
                depth += 1
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


def x_parse_line__mutmut_80(line: str, line_number: int = 0) -> Optional[Statement]:
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
                depth -= 2
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


def x_parse_line__mutmut_81(line: str, line_number: int = 0) -> Optional[Statement]:
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
                current_op.append(None)
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


def x_parse_line__mutmut_82(line: str, line_number: int = 0) -> Optional[Statement]:
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
            elif char == "," or depth == 0:
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


def x_parse_line__mutmut_83(line: str, line_number: int = 0) -> Optional[Statement]:
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
            elif char != "," and depth == 0:
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


def x_parse_line__mutmut_84(line: str, line_number: int = 0) -> Optional[Statement]:
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
            elif char == "XX,XX" and depth == 0:
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


def x_parse_line__mutmut_85(line: str, line_number: int = 0) -> Optional[Statement]:
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
            elif char == "," and depth != 0:
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


def x_parse_line__mutmut_86(line: str, line_number: int = 0) -> Optional[Statement]:
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
            elif char == "," and depth == 1:
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


def x_parse_line__mutmut_87(line: str, line_number: int = 0) -> Optional[Statement]:
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
                operand_strs.append(None)
                current_op = []
            else:
                current_op.append(char)
        if current_op:
            operand_strs.append("".join(current_op).strip())

        for op_str in operand_strs:
            if op_str:
                stmt.operands.append(parse_operand(op_str))

    return stmt


def x_parse_line__mutmut_88(line: str, line_number: int = 0) -> Optional[Statement]:
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
                operand_strs.append("".join(None).strip())
                current_op = []
            else:
                current_op.append(char)
        if current_op:
            operand_strs.append("".join(current_op).strip())

        for op_str in operand_strs:
            if op_str:
                stmt.operands.append(parse_operand(op_str))

    return stmt


def x_parse_line__mutmut_89(line: str, line_number: int = 0) -> Optional[Statement]:
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
                operand_strs.append("XXXX".join(current_op).strip())
                current_op = []
            else:
                current_op.append(char)
        if current_op:
            operand_strs.append("".join(current_op).strip())

        for op_str in operand_strs:
            if op_str:
                stmt.operands.append(parse_operand(op_str))

    return stmt


def x_parse_line__mutmut_90(line: str, line_number: int = 0) -> Optional[Statement]:
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
                current_op = None
            else:
                current_op.append(char)
        if current_op:
            operand_strs.append("".join(current_op).strip())

        for op_str in operand_strs:
            if op_str:
                stmt.operands.append(parse_operand(op_str))

    return stmt


def x_parse_line__mutmut_91(line: str, line_number: int = 0) -> Optional[Statement]:
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
                current_op.append(None)
        if current_op:
            operand_strs.append("".join(current_op).strip())

        for op_str in operand_strs:
            if op_str:
                stmt.operands.append(parse_operand(op_str))

    return stmt


def x_parse_line__mutmut_92(line: str, line_number: int = 0) -> Optional[Statement]:
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
            operand_strs.append(None)

        for op_str in operand_strs:
            if op_str:
                stmt.operands.append(parse_operand(op_str))

    return stmt


def x_parse_line__mutmut_93(line: str, line_number: int = 0) -> Optional[Statement]:
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
            operand_strs.append("".join(None).strip())

        for op_str in operand_strs:
            if op_str:
                stmt.operands.append(parse_operand(op_str))

    return stmt


def x_parse_line__mutmut_94(line: str, line_number: int = 0) -> Optional[Statement]:
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
            operand_strs.append("XXXX".join(current_op).strip())

        for op_str in operand_strs:
            if op_str:
                stmt.operands.append(parse_operand(op_str))

    return stmt


def x_parse_line__mutmut_95(line: str, line_number: int = 0) -> Optional[Statement]:
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
                stmt.operands.append(None)

    return stmt


def x_parse_line__mutmut_96(line: str, line_number: int = 0) -> Optional[Statement]:
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
                stmt.operands.append(parse_operand(None))

    return stmt

mutants_x_parse_line__mutmut['_mutmut_orig'] = x_parse_line__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_1'] = x_parse_line__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_2'] = x_parse_line__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_3'] = x_parse_line__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_4'] = x_parse_line__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_5'] = x_parse_line__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_6'] = x_parse_line__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_7'] = x_parse_line__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_8'] = x_parse_line__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_9'] = x_parse_line__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_10'] = x_parse_line__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_11'] = x_parse_line__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_12'] = x_parse_line__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_13'] = x_parse_line__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_14'] = x_parse_line__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_15'] = x_parse_line__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_16'] = x_parse_line__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_17'] = x_parse_line__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_18'] = x_parse_line__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_19'] = x_parse_line__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_20'] = x_parse_line__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_21'] = x_parse_line__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_22'] = x_parse_line__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_23'] = x_parse_line__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_24'] = x_parse_line__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_25'] = x_parse_line__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_26'] = x_parse_line__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_27'] = x_parse_line__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_28'] = x_parse_line__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_29'] = x_parse_line__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_30'] = x_parse_line__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_31'] = x_parse_line__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_32'] = x_parse_line__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_33'] = x_parse_line__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_34'] = x_parse_line__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_35'] = x_parse_line__mutmut_35 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_36'] = x_parse_line__mutmut_36 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_37'] = x_parse_line__mutmut_37 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_38'] = x_parse_line__mutmut_38 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_39'] = x_parse_line__mutmut_39 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_40'] = x_parse_line__mutmut_40 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_41'] = x_parse_line__mutmut_41 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_42'] = x_parse_line__mutmut_42 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_43'] = x_parse_line__mutmut_43 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_44'] = x_parse_line__mutmut_44 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_45'] = x_parse_line__mutmut_45 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_46'] = x_parse_line__mutmut_46 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_47'] = x_parse_line__mutmut_47 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_48'] = x_parse_line__mutmut_48 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_49'] = x_parse_line__mutmut_49 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_50'] = x_parse_line__mutmut_50 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_51'] = x_parse_line__mutmut_51 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_52'] = x_parse_line__mutmut_52 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_53'] = x_parse_line__mutmut_53 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_54'] = x_parse_line__mutmut_54 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_55'] = x_parse_line__mutmut_55 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_56'] = x_parse_line__mutmut_56 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_57'] = x_parse_line__mutmut_57 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_58'] = x_parse_line__mutmut_58 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_59'] = x_parse_line__mutmut_59 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_60'] = x_parse_line__mutmut_60 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_61'] = x_parse_line__mutmut_61 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_62'] = x_parse_line__mutmut_62 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_63'] = x_parse_line__mutmut_63 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_64'] = x_parse_line__mutmut_64 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_65'] = x_parse_line__mutmut_65 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_66'] = x_parse_line__mutmut_66 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_67'] = x_parse_line__mutmut_67 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_68'] = x_parse_line__mutmut_68 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_69'] = x_parse_line__mutmut_69 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_70'] = x_parse_line__mutmut_70 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_71'] = x_parse_line__mutmut_71 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_72'] = x_parse_line__mutmut_72 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_73'] = x_parse_line__mutmut_73 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_74'] = x_parse_line__mutmut_74 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_75'] = x_parse_line__mutmut_75 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_76'] = x_parse_line__mutmut_76 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_77'] = x_parse_line__mutmut_77 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_78'] = x_parse_line__mutmut_78 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_79'] = x_parse_line__mutmut_79 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_80'] = x_parse_line__mutmut_80 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_81'] = x_parse_line__mutmut_81 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_82'] = x_parse_line__mutmut_82 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_83'] = x_parse_line__mutmut_83 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_84'] = x_parse_line__mutmut_84 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_85'] = x_parse_line__mutmut_85 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_86'] = x_parse_line__mutmut_86 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_87'] = x_parse_line__mutmut_87 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_88'] = x_parse_line__mutmut_88 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_89'] = x_parse_line__mutmut_89 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_90'] = x_parse_line__mutmut_90 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_91'] = x_parse_line__mutmut_91 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_92'] = x_parse_line__mutmut_92 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_93'] = x_parse_line__mutmut_93 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_94'] = x_parse_line__mutmut_94 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_95'] = x_parse_line__mutmut_95 # type: ignore # mutmut generated
mutants_x_parse_line__mutmut['x_parse_line__mutmut_96'] = x_parse_line__mutmut_96 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_assembly__mutmut)
def parse_assembly(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_orig(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_1(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = None
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_2(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(None, start=1):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_3(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=None):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_4(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(start=1):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_5(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), ):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_6(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=2):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_7(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = None
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_8(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(None, line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_9(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(line, line_number=None)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_10(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(line_number=line_no)
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_11(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(line, )
        if stmt is not None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_12(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(line, line_number=line_no)
        if stmt is None:
            statements.append(stmt)
    return statements


def x_parse_assembly__mutmut_13(source: str) -> list[Statement]:
    """Parse complete MSP430 assembly source text into statements."""
    statements: list[Statement] = []
    for line_no, line in enumerate(source.splitlines(), start=1):
        stmt = parse_line(line, line_number=line_no)
        if stmt is not None:
            statements.append(None)
    return statements

mutants_x_parse_assembly__mutmut['_mutmut_orig'] = x_parse_assembly__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_1'] = x_parse_assembly__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_2'] = x_parse_assembly__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_3'] = x_parse_assembly__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_4'] = x_parse_assembly__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_5'] = x_parse_assembly__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_6'] = x_parse_assembly__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_7'] = x_parse_assembly__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_8'] = x_parse_assembly__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_9'] = x_parse_assembly__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_10'] = x_parse_assembly__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_11'] = x_parse_assembly__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_12'] = x_parse_assembly__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_assembly__mutmut['x_parse_assembly__mutmut_13'] = x_parse_assembly__mutmut_13 # type: ignore # mutmut generated
