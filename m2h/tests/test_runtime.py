# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

from m2h.emitter import HackEmitter
from m2h.parser import parse_assembly
from m2h.runtime import (
    generate_div_routines,
    generate_epilog_routines,
    generate_mpy_routine,
    generate_shift_routines,
    generate_sll_routine,
    get_required_runtime_routines,
)


def test_generate_mpy_routine() -> None:
    lines = generate_mpy_routine()
    assert "(__mspabi_mpyi)" in lines
    assert "(__mulhi3)" in lines
    assert "@__M2H_LIB_RES" in lines
    assert "@R13" in lines
    assert "@R14" not in lines


def test_generate_div_routines() -> None:
    lines = generate_div_routines()
    assert "(__m2h_udivmod)" in lines
    assert "(__mspabi_divu)" in lines
    assert "(__mspabi_remu)" in lines
    assert "(__mspabi_divi)" in lines
    assert "(__mspabi_remi)" in lines
    assert "@R13" in lines
    assert "@R14" not in lines


def test_generate_epilog_routines() -> None:
    lines = generate_epilog_routines()
    assert "(__mspabi_func_epilog_1)" in lines
    assert "(__mspabi_func_epilog_2)" in lines
    assert "(__mspabi_func_epilog_7)" in lines
    assert "@R4" in lines
    assert "@R10" in lines


def test_generate_shift_routines() -> None:
    lines = generate_shift_routines()
    assert "(__m2h_rrc)" in lines
    assert "(__m2h_rra)" in lines
    assert "@__M2H_LIB_RES" in lines


def test_generate_sll_routine() -> None:
    lines = generate_sll_routine()
    assert "(__mspabi_slli)" in lines
    assert "(__ashlhi3)" in lines
    assert "@R12" in lines
    assert "@R13" in lines


def test_get_required_runtime_routines_empty() -> None:
    routines = get_required_runtime_routines({"main", "foo", "printf"})
    assert routines == []


def test_get_required_runtime_routines_mpy() -> None:
    routines = get_required_runtime_routines({"__mspabi_mpyi"})
    assert any("(__mspabi_mpyi)" in line for line in routines)
    assert not any("(__m2h_udivmod)" in line for line in routines)


def test_get_required_runtime_routines_div() -> None:
    routines = get_required_runtime_routines({"__divhi3"})
    assert any("(__m2h_udivmod)" in line for line in routines)
    assert not any("(__mspabi_mpyi)" in line for line in routines)


def test_get_required_runtime_routines_epilog() -> None:
    routines = get_required_runtime_routines({"__mspabi_func_epilog_2"})
    assert any("(__mspabi_func_epilog_2)" in line for line in routines)
    assert not any("(__mspabi_mpyi)" in line for line in routines)


def test_get_required_runtime_routines_shift() -> None:
    routines = get_required_runtime_routines({"__m2h_rra"})
    assert any("(__m2h_rra)" in line for line in routines)
    assert not any("(__mspabi_mpyi)" in line for line in routines)


def test_get_required_runtime_routines_sll() -> None:
    routines = get_required_runtime_routines({"__mspabi_slli"})
    assert any("(__mspabi_slli)" in line for line in routines)
    assert not any("(__mspabi_mpyi)" in line for line in routines)


def test_emitter_auto_includes_runtime_helpers() -> None:
    source = """
    .globl main
main:
    mov #6, r12
    mov #7, r13
    call #__mspabi_mpyi
    mov #3, r13
    call #__mspabi_divi
    mov #2, r13
    call #__mspabi_slli
    rra r12
    br #__mspabi_func_epilog_2
    """
    stmts = parse_assembly(source)
    emitter = HackEmitter(include_crt0=False)
    asm = emitter.emit_program(stmts)
    assert "(__mspabi_mpyi)" in asm
    assert "(__m2h_udivmod)" in asm
    assert "(__mspabi_divi)" in asm
    assert "(__mspabi_func_epilog_2)" in asm
    assert "(__m2h_rra)" in asm
    assert "(__mspabi_slli)" in asm
