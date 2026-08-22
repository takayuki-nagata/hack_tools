# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

import pytest

from m2h.parser import (
    OperandType,
    clean_line,
    is_register,
    normalize_register_name,
    parse_assembly,
    parse_line,
    parse_operand,
)


def test_normalize_register_name() -> None:
    assert normalize_register_name("sp") == "r1"
    assert normalize_register_name("SP") == "r1"
    assert normalize_register_name("pc") == "r0"
    assert normalize_register_name("sr") == "r2"
    assert normalize_register_name("cg") == "r3"
    assert normalize_register_name("r4") == "r4"
    assert normalize_register_name("R15") == "r15"


def test_is_register() -> None:
    assert is_register("r0")
    assert is_register("r15")
    assert is_register("SP")
    assert is_register("pc")
    assert not is_register("r16")
    assert not is_register("foo")


def test_parse_operand_valid() -> None:
    # Immediate
    op = parse_operand("#123")
    assert op.op_type == OperandType.IMMEDIATE
    assert op.value == "123"
    assert str(op) == "#123"

    # Register
    op = parse_operand("r4")
    assert op.op_type == OperandType.REGISTER
    assert op.value == "r4"
    assert str(op) == "r4"

    # Indirect
    op = parse_operand("@r5")
    assert op.op_type == OperandType.INDIRECT
    assert op.value == "r5"
    assert str(op) == "@r5"

    # Indirect Autoincrement
    op = parse_operand("@r5+")
    assert op.op_type == OperandType.INDIRECT_AUTOINC
    assert op.value == "r5"
    assert str(op) == "@r5+"

    # Indexed
    op = parse_operand("4(r1)")
    assert op.op_type == OperandType.INDEXED
    assert op.value == "4"
    assert op.reg == "r1"
    assert str(op) == "4(r1)"

    # Absolute &var
    op = parse_operand("&my_var")
    assert op.op_type == OperandType.ABSOLUTE
    assert op.value == "my_var"

    # Absolute symbol
    op = parse_operand("my_func")
    assert op.op_type == OperandType.ABSOLUTE
    assert op.value == "my_func"
    assert str(op) == "my_func"


def test_parse_operand_invalid() -> None:
    with pytest.raises(ValueError, match="Empty operand"):
        parse_operand("")

    with pytest.raises(ValueError, match="Invalid register in autoincrement"):
        parse_operand("@notareg+")

    with pytest.raises(ValueError, match="Invalid register in indirect"):
        parse_operand("@notareg")

    with pytest.raises(ValueError, match="Invalid register in indexed"):
        parse_operand("4(notareg)")


def test_clean_line() -> None:
    assert clean_line("  mov r4, r5 ; comment  ") == "mov r4, r5"
    assert clean_line("  add r4, r5 // comment  ") == "add r4, r5"
    assert clean_line("// whole comment") == ""
    assert clean_line("   ") == ""


def test_parse_line_labels_and_directives() -> None:
    # Empty
    assert parse_line("") is None
    assert parse_line("  // comment") is None

    # Label only
    stmt = parse_line("main:")
    assert stmt is not None
    assert stmt.label == "main"
    assert stmt.mnemonic is None

    # Label with instruction
    stmt = parse_line("main: mov #0, r12")
    assert stmt is not None
    assert stmt.label == "main"
    assert stmt.mnemonic == "mov"
    assert len(stmt.operands) == 2

    # Directive without args
    stmt = parse_line(".text")
    assert stmt is not None
    assert stmt.directive == ".text"
    assert len(stmt.directive_args) == 0

    # Directive with args
    stmt = parse_line(".globl main, foo")
    assert stmt is not None
    assert stmt.directive == ".globl"
    assert stmt.directive_args == ["main", "foo"]


def test_parse_line_instructions() -> None:
    # Suffix stripping (.w, .b)
    stmt = parse_line("mov.w #1, r14")
    assert stmt is not None
    assert stmt.mnemonic == "mov"

    stmt = parse_line("mov.b #1, r14")
    assert stmt is not None
    assert stmt.mnemonic == "mov"

    # Indexed with comma in offset or complex expression
    stmt = parse_line("mov 4(r1), 2(r5)")
    assert stmt is not None
    assert len(stmt.operands) == 2
    assert stmt.operands[0].op_type == OperandType.INDEXED
    assert stmt.operands[1].op_type == OperandType.INDEXED


def test_parse_assembly() -> None:
    source = """
    .text
    .globl main
main:
    mov #0, r12
    ret
    """
    stmts = parse_assembly(source)
    assert len(stmts) == 5
    assert stmts[0].directive == ".text"
    assert stmts[1].directive == ".globl"
    assert stmts[2].label == "main"
    assert stmts[3].mnemonic == "mov"
    assert stmts[4].mnemonic == "ret"
