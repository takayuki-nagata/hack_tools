# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

from m2h.crt0 import generate_crt0


def test_generate_crt0_default() -> None:
    lines = generate_crt0()
    assert "@16384" in lines
    assert "@SP" in lines
    assert "@main" in lines
    assert "(__HALT)" in lines


def test_generate_crt0_custom() -> None:
    lines = generate_crt0(stack_start=512, entry_point="_start")
    assert "@512" in lines
    assert "@_start" in lines
