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

    # Load Autoincrement (word by default +2, byte +1)
    assert emitter.emit_load_operand(Operand(OperandType.INDIRECT_AUTOINC, "r5")) == [
        "@R5",
        "A=M",
        "D=M",
        "@R5",
        "M=M+1",
        "@R5",
        "M=M+1",
    ]
    assert emitter.emit_load_operand(Operand(OperandType.INDIRECT_AUTOINC, "r5"), is_byte=True) == [
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

    s = parse_line("jhs .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JGE"]

    s = parse_line("jc .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JGE"]

    s = parse_line("jl .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JLT"]

    s = parse_line("jn .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JLT"]

    s = parse_line("jlo .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JLT"]

    s = parse_line("jnc .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "D;JLT"]

    s = parse_line("jmp .L2")
    assert s is not None
    assert emitter.emit_statement(s) == ["@DOT_L2", "0;JMP"]

    # push / pop
    s = parse_line("push r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@R12", "D=M", "@SP", "M=M-1", "A=M", "M=D"]

    s = parse_line("pop r12")
    assert s is not None
    assert emitter.emit_statement(s) == ["@SP", "A=M", "D=M", "@SP", "M=M+1", "@R12", "M=D"]

    # call / ret / nop
    s = parse_line("call #foo")
    assert s is not None
    out = emitter.emit_statement(s)
    assert "@foo" in out
    assert "0;JMP" in out

    s = parse_line("ret")
    assert s is not None
    assert emitter.emit_statement(s) == ["@SP", "A=M", "D=M", "@SP", "M=M+1", "A=D", "0;JMP"]

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

    s = parse_line("call r12")
    assert s is not None
    code = emitter.emit_statement(s)
    assert "@R12" in code
    assert "A=M" in code

    s = parse_line("call 0(r4)")
    assert s is not None
    code = emitter.emit_statement(s)
    assert "A=D" in code

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

    s = parse_line("rra")
    assert s is not None
    with pytest.raises(ValueError, match="rra requires 1 operand"):
        emitter.emit_statement(s)

    # Condition / Status instructions
    for cond in ("clrc", "setc", "clrn", "setn", "clrz", "setz", "dint", "eint", "nop"):
        s = parse_line(cond)
        assert s is not None
        code = emitter.emit_statement(s)
        assert f"// {cond}" in code

    # Shift right instructions
    s = parse_line("rra r12")
    assert s is not None
    code = emitter.emit_statement(s)
    assert "@__m2h_rra" in code

    s = parse_line("rrc 4(r1)")
    assert s is not None
    code = emitter.emit_statement(s)
    assert "@__m2h_rrc" in code

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
    assert "@16384" in asm
    assert "@42" in asm
    assert "0;JMP" in asm


def test_emit_operand_symbol_and_negative_offsets() -> None:
    emitter = HackEmitter()

    # Immediate with positive and negative symbol offsets
    s1 = parse_line("mov #sym+4, r12")
    assert s1 is not None
    code1 = emitter.emit_statement(s1)
    assert any("D=D+A" in line for line in code1)

    s2 = parse_line("mov #sym-2, r12")
    assert s2 is not None
    code2 = emitter.emit_statement(s2)
    assert any("D=D-A" in line for line in code2)

    # Indexed load with -1, negative offset, 1, positive offset, symbol offset
    s3 = parse_line("mov -1(r4), r12")
    assert s3 is not None
    code3 = emitter.emit_statement(s3)
    assert "D=-1" in code3

    s4 = parse_line("mov -4(r4), r12")
    assert s4 is not None
    code4 = emitter.emit_statement(s4)
    assert "D=-A" in code4

    s5 = parse_line("mov 1(r4), r12")
    assert s5 is not None
    code5 = emitter.emit_statement(s5)
    assert "@1" in code5

    s6 = parse_line("mov 4(r4), r12")
    assert s6 is not None
    code6 = emitter.emit_statement(s6)
    assert "@4" in code6

    s7 = parse_line("mov offset(r4), r12")
    assert s7 is not None
    code7 = emitter.emit_statement(s7)
    assert "@offset" in code7

    # Indexed store with -1, negative offset, 1, positive offset, symbol offset
    s8 = parse_line("mov r12, -1(r4)")
    assert s8 is not None
    code8 = emitter.emit_statement(s8)
    assert "D=-1" in code8

    s9 = parse_line("mov r12, -4(r4)")
    assert s9 is not None
    code9 = emitter.emit_statement(s9)
    assert "D=-A" in code9

    s10 = parse_line("mov r12, 1(r4)")
    assert s10 is not None
    code10 = emitter.emit_statement(s10)
    assert "@1" in code10

    s11 = parse_line("mov r12, 4(r4)")
    assert s11 is not None
    code11 = emitter.emit_statement(s11)
    assert "@4" in code11

    s12 = parse_line("mov r12, offset(r4)")
    assert s12 is not None
    code12 = emitter.emit_statement(s12)
    assert "@offset" in code12

    # Absolute load with sym+offset and sym-offset
    s13 = parse_line("mov &sym+4, r12")
    assert s13 is not None
    code13 = emitter.emit_statement(s13)
    assert any("A=D+A" in line for line in code13)

    s14 = parse_line("mov &sym-2, r12")
    assert s14 is not None
    code14 = emitter.emit_statement(s14)
    assert any("A=D-A" in line for line in code14)

    # Absolute store with sym+offset and sym-offset
    s15 = parse_line("mov r12, &sym+4")
    assert s15 is not None
    code15 = emitter.emit_statement(s15)
    assert any("D=D+A" in line for line in code15)

    s16 = parse_line("mov r12, &sym-2")
    assert s16 is not None
    code16 = emitter.emit_statement(s16)
    assert any("D=D-A" in line for line in code16)
