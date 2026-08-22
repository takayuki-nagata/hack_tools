# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

import pytest

from m2h.emitter import (
    HackEmitter,
    reg_to_hack_symbol,
    sanitize_symbol,
)
from m2h.parser import Operand, OperandType, parse_assembly, parse_line


def test_sanitize_symbol() -> None:
    assert sanitize_symbol("") == ""
    assert sanitize_symbol(".L2") == "DOT_L2"
    assert sanitize_symbol("main") == "main"


def test_reg_to_hack_symbol() -> None:
    assert reg_to_hack_symbol("r0") == "R0"
    assert reg_to_hack_symbol("pc") == "R0"
    assert reg_to_hack_symbol("r1") == "SP"
    assert reg_to_hack_symbol("sp") == "SP"
    assert reg_to_hack_symbol("r2") == "R2"
    assert reg_to_hack_symbol("sr") == "R2"
    assert reg_to_hack_symbol("r3") == "R3"
    assert reg_to_hack_symbol("cg") == "R3"
    assert reg_to_hack_symbol("r4") == "R4"
    assert reg_to_hack_symbol("r15") == "R15"


def test_emit_operands() -> None:
    emitter = HackEmitter()

    # Load Register
    assert emitter.emit_load_operand(Operand(OperandType.REGISTER, "r4")) == ["@R4", "D=M"]
    # Store Register
    assert emitter.emit_store_operand(Operand(OperandType.REGISTER, "r4")) == ["@R4", "M=D"]

    # Load Immediate
    assert emitter.emit_load_operand(Operand(OperandType.IMMEDIATE, "42")) == ["@42", "D=A"]
    with pytest.raises(ValueError, match="Cannot store"):
        emitter.emit_store_operand(Operand(OperandType.IMMEDIATE, "42"))

    # Load/Store Indirect
    assert emitter.emit_load_operand(Operand(OperandType.INDIRECT, "r5")) == ["@R5", "A=M", "D=M"]
    assert emitter.emit_store_operand(Operand(OperandType.INDIRECT, "r5")) == ["@R5", "A=M", "M=D"]

    # Load Autoincrement
    assert emitter.emit_load_operand(Operand(OperandType.INDIRECT_AUTOINC, "r5")) == [
        "@R5",
        "A=M",
        "D=M",
        "@R5",
        "M=M+1",
    ]

    # Load/Store Indexed 0
    assert emitter.emit_load_operand(Operand(OperandType.INDEXED, "0", "r1")) == [
        "@SP",
        "A=M",
        "D=M",
    ]
    assert emitter.emit_store_operand(Operand(OperandType.INDEXED, "0", "r1")) == [
        "@SP",
        "A=M",
        "M=D",
    ]

    # Load/Store Indexed non-0
    assert emitter.emit_load_operand(Operand(OperandType.INDEXED, "4", "r1")) == [
        "@4",
        "D=A",
        "@SP",
        "A=D+M",
        "D=M",
    ]
    stored = emitter.emit_store_operand(Operand(OperandType.INDEXED, "4", "r1"))
    assert "@__M2H_TMP_VAL" in stored
    assert "@SP" in stored

    # Load/Store Absolute
    assert emitter.emit_load_operand(Operand(OperandType.ABSOLUTE, "g_var")) == ["@g_var", "D=M"]
    assert emitter.emit_store_operand(Operand(OperandType.ABSOLUTE, "g_var")) == ["@g_var", "M=D"]


def test_emit_instructions() -> None:
    emitter = HackEmitter(include_crt0=False)

    # Label only
    s = parse_line("my_label:")
    assert s is not None
    assert emitter.emit_statement(s) == ["(my_label)"]

    # Directives (.word)
    s = parse_line(".word 10, 20")
    assert s is not None
    assert "@10" in emitter.emit_statement(s)

    # mov
    s = parse_line("mov #1, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@1", "D=A", "@R12", "M=D"]

    # add
    s = parse_line("add #1, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=M+1"]

    s = parse_line("add r13, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R13", "D=M", "@R12", "M=D+M"]

    s = parse_line("add r13, @r12")
    assert s is not None
    assert "@__M2H_TMP_VAL" in emitter.emit_statement(s)

    # sub
    s = parse_line("sub #1, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=M-1"]

    s = parse_line("sub r13, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R13", "D=M", "@R12", "M=M-D"]

    s = parse_line("sub r13, @r12")
    assert s is not None
    assert "@__M2H_TMP_VAL" in emitter.emit_statement(s)

    # and
    s = parse_line("and r13, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R13", "D=M", "@R12", "M=D&M"]

    s = parse_line("and r13, @r12")
    assert s is not None
    assert "@__M2H_TMP_VAL" in emitter.emit_statement(s)

    # bis (OR)
    s = parse_line("bis r13, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R13", "D=M", "@R12", "M=D|M"]

    s = parse_line("bis r13, @r12")
    assert s is not None
    assert "@__M2H_TMP_VAL" in emitter.emit_statement(s)

    # bic (Clear: dst & ~src)
    s = parse_line("bic r13, r12")
    assert s is not None
    assert "D=!D" in emitter.emit_statement(s)

    s = parse_line("bic r13, @r12")
    assert s is not None
    assert "@__M2H_TMP_VAL" in emitter.emit_statement(s)

    # xor
    s = parse_line("xor r13, r12")
    assert s is not None
    assert "@__M2H_TMP_OR" in emitter.emit_statement(s)

    # clr
    s = parse_line("clr r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@0", "D=A", "@R12", "M=D"]

    # Negative and constant immediates loading
    assert emitter.emit_load_operand(Operand(OperandType.IMMEDIATE, "0")) == ["@0", "D=A"]
    assert emitter.emit_load_operand(Operand(OperandType.IMMEDIATE, "1")) == ["@1", "D=A"]
    assert emitter.emit_load_operand(Operand(OperandType.IMMEDIATE, "-1")) == ["D=-1"]
    assert emitter.emit_load_operand(Operand(OperandType.IMMEDIATE, "-5")) == ["@5", "D=-A"]
    assert emitter.emit_load_operand(Operand(OperandType.IMMEDIATE, "my_func")) == [
        "@my_func",
        "D=A",
    ]

    # add / sub with -1
    s = parse_line("add #-1, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=M-1"]

    s = parse_line("sub #-1, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=M+1"]

    # inc / incd / dec / decd
    s = parse_line("inc r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=M+1"]

    s = parse_line("incd r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=M+1", "@R12", "M=M+1"]

    s = parse_line("inc @r12")
    assert s is not None
    assert "D=D+1" in emitter.emit_statement(s)

    s = parse_line("dec r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=M-1"]

    s = parse_line("decd r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=M-1", "@R12", "M=M-1"]

    s = parse_line("dec @r12")
    assert s is not None
    assert "D=D-1" in emitter.emit_statement(s)

    # bit (Bit Test)
    s = parse_line("bit r13, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R13", "D=M", "@R12", "D=D&M"]

    s = parse_line("bit r13, @r12")
    assert s is not None
    assert "@__M2H_TMP_VAL" in emitter.emit_statement(s)

    s = parse_line("dec @r12")
    assert s is not None
    assert "D=D-1" in emitter.emit_statement(s)

    # inv / neg
    s = parse_line("inv r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=!M"]

    s = parse_line("inv @r12")
    assert s is not None
    assert "D=!D" in emitter.emit_statement(s)

    s = parse_line("neg r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "M=-M"]

    s = parse_line("neg @r12")
    assert s is not None
    assert "D=-D" in emitter.emit_statement(s)

    # tst
    s = parse_line("tst r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "D=M"]

    # cmp
    s = parse_line("cmp r13, r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R13", "D=M", "@R12", "D=M-D"]

    s = parse_line("cmp r13, @r12")
    assert s is not None
    assert "@__M2H_TMP_VAL" in emitter.emit_statement(s)

    # Branches
    s = parse_line("jeq .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JEQ"]

    s = parse_line("jz .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JEQ"]

    s = parse_line("jne .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JNE"]

    s = parse_line("jnz .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JNE"]

    s = parse_line("jge .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JGE"]

    s = parse_line("jl .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JLT"]

    s = parse_line("jn .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JLT"]

    s = parse_line("jmp .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "0;JMP"]

    # push / pop
    s = parse_line("push r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"]

    s = parse_line("pop r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@SP", "M=M-1", "A=M", "D=M", "@R12", "M=D"]

    # call / ret / nop
    s = parse_line("call #foo")
    assert s is not None
    out = emitter.emit_statement(s)
    assert "@foo" in out
    assert "0;JMP" in out

    s = parse_line("ret")
    assert s is not None
    assert emitter.emit_statement(s) == ["@SP", "M=M-1", "A=M", "A=M", "0;JMP"]

    s = parse_line("nop")
    assert s is not None
    assert emitter.emit_statement(s) == ["// nop"]

    # rla / rlc
    s = parse_line("rla r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "D=M", "@R12", "M=D+M"]

    s = parse_line("rla @r12")
    assert s is not None
    assert "D=D+D" in emitter.emit_statement(s)

    s = parse_line("rlc r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "D=M", "@R12", "M=D+M"]

    # br (branch)
    s = parse_line("br r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "A=M", "0;JMP"]

    s = parse_line("br #my_func")
    assert s is not None
    assert emitter.emit_statement(s) == ["@my_func", "0;JMP"]

    s = parse_line("br @r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "A=M", "D=M", "A=D", "0;JMP"]


def test_emit_errors() -> None:
    emitter = HackEmitter()

    # Invalid operand count
    s = parse_line("mov r1")
    assert s is not None
    with pytest.raises(ValueError, match="mov requires 2 operands"):
        emitter.emit_statement(s)

    s = parse_line("add r1")
    assert s is not None
    with pytest.raises(ValueError, match="add requires 2 operands"):
        emitter.emit_statement(s)

    s = parse_line("sub r1")
    assert s is not None
    with pytest.raises(ValueError, match="sub requires 2 operands"):
        emitter.emit_statement(s)

    s = parse_line("and r1")
    assert s is not None
    with pytest.raises(ValueError, match="and requires 2 operands"):
        emitter.emit_statement(s)

    s = parse_line("bis r1")
    assert s is not None
    with pytest.raises(ValueError, match="bis requires 2 operands"):
        emitter.emit_statement(s)

    s = parse_line("bic r1")
    assert s is not None
    with pytest.raises(ValueError, match="bic requires 2 operands"):
        emitter.emit_statement(s)

    s = parse_line("xor r1")
    assert s is not None
    with pytest.raises(ValueError, match="xor requires 2 operands"):
        emitter.emit_statement(s)

    s = parse_line("clr")
    assert s is not None
    with pytest.raises(ValueError, match="clr requires 1 operand"):
        emitter.emit_statement(s)

    s = parse_line("inc")
    assert s is not None
    with pytest.raises(ValueError, match="inc requires 1 operand"):
        emitter.emit_statement(s)

    s = parse_line("dec")
    assert s is not None
    with pytest.raises(ValueError, match="dec requires 1 operand"):
        emitter.emit_statement(s)

    s = parse_line("inv")
    assert s is not None
    with pytest.raises(ValueError, match="inv requires 1 operand"):
        emitter.emit_statement(s)

    s = parse_line("neg")
    assert s is not None
    with pytest.raises(ValueError, match="neg requires 1 operand"):
        emitter.emit_statement(s)

    s = parse_line("tst")
    assert s is not None
    with pytest.raises(ValueError, match="tst requires 1 operand"):
        emitter.emit_statement(s)

    s = parse_line("cmp r1")
    assert s is not None
    with pytest.raises(ValueError, match="cmp requires 2 operands"):
        emitter.emit_statement(s)

    s = parse_line("jeq")
    assert s is not None
    with pytest.raises(ValueError, match="jeq requires 1 target"):
        emitter.emit_statement(s)

    s = parse_line("jne")
    assert s is not None
    with pytest.raises(ValueError, match="jne requires 1 target"):
        emitter.emit_statement(s)

    s = parse_line("jge")
    assert s is not None
    with pytest.raises(ValueError, match="jge requires 1 target"):
        emitter.emit_statement(s)

    s = parse_line("jl")
    assert s is not None
    with pytest.raises(ValueError, match="jl requires 1 target"):
        emitter.emit_statement(s)

    s = parse_line("jmp")
    assert s is not None
    with pytest.raises(ValueError, match="jmp requires 1 target"):
        emitter.emit_statement(s)

    s = parse_line("push")
    assert s is not None
    with pytest.raises(ValueError, match="push requires 1 operand"):
        emitter.emit_statement(s)

    s = parse_line("pop")
    assert s is not None
    with pytest.raises(ValueError, match="pop requires 1 operand"):
        emitter.emit_statement(s)

    s = parse_line("call")
    assert s is not None
    with pytest.raises(ValueError, match="call requires 1 target"):
        emitter.emit_statement(s)

    s = parse_line("rla")
    assert s is not None
    with pytest.raises(ValueError, match="rla requires 1 operand"):
        emitter.emit_statement(s)

    s = parse_line("br")
    assert s is not None
    with pytest.raises(ValueError, match="br requires 1 target"):
        emitter.emit_statement(s)

    s = parse_line("bit r1")
    assert s is not None
    with pytest.raises(ValueError, match="bit requires 2 operands"):
        emitter.emit_statement(s)

    s = parse_line("invalid_mnemonic r1")
    assert s is not None
    with pytest.raises(ValueError, match="Unsupported mnemonic"):
        emitter.emit_statement(s)


def test_emit_program() -> None:
    source = """
    mov #42, r12
    ret
    """
    stmts = parse_assembly(source)
    emitter = HackEmitter(include_crt0=True)
    asm = emitter.emit_program(stmts)
    assert "@256" in asm
    assert "@42" in asm
    assert "0;JMP" in asm
