# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

"""Runtime startup code generator (crt0) for Hack programs."""


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_generate_crt0__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_generate_crt0__mutmut)
def generate_crt0(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_orig(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_1(stack_start: int = 257, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_2(stack_start: int = 256, entry_point: str = "XXmainXX") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_3(stack_start: int = 256, entry_point: str = "MAIN") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_4(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "XX// === Runtime Startup (crt0) ===XX",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_5(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === runtime startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_6(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === RUNTIME STARTUP (CRT0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_7(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "XXD=AXX",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_8(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "d=a",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_9(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "XX@SPXX",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_10(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@sp",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_11(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "XXM=DXX",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_12(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "m=d",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_13(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "XX// Call entry pointXX",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_14(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_15(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// CALL ENTRY POINT",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_16(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "XX@__HALTXX",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_17(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__halt",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_18(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "XXD=AXX",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_19(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "d=a",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_20(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "XX@SPXX",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_21(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@sp",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_22(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "XXA=MXX",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_23(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "a=m",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_24(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "XXM=DXX",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_25(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "m=d",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_26(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "XX@SPXX",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_27(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@sp",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_28(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "XXM=M+1XX",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_29(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "m=m+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_30(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "XX0;JMPXX",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_31(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;jmp",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_32(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "XX(__HALT)XX",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_33(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__halt)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_34(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "XX@__HALTXX",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_35(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__halt",
        "0;JMP",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_36(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "XX0;JMPXX",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_37(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;jmp",
        "// === End of Startup ===",
    ]


def x_generate_crt0__mutmut_38(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "XX// === End of Startup ===XX",
    ]


def x_generate_crt0__mutmut_39(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === end of startup ===",
    ]


def x_generate_crt0__mutmut_40(stack_start: int = 256, entry_point: str = "main") -> list[str]:
    """Generate Hack assembly startup sequence (crt0)."""
    return [
        "// === Runtime Startup (crt0) ===",
        f"@{stack_start}",
        "D=A",
        "@SP",
        "M=D",
        "// Call entry point",
        "@__HALT",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === END OF STARTUP ===",
    ]

mutants_x_generate_crt0__mutmut['_mutmut_orig'] = x_generate_crt0__mutmut_orig # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_1'] = x_generate_crt0__mutmut_1 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_2'] = x_generate_crt0__mutmut_2 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_3'] = x_generate_crt0__mutmut_3 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_4'] = x_generate_crt0__mutmut_4 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_5'] = x_generate_crt0__mutmut_5 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_6'] = x_generate_crt0__mutmut_6 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_7'] = x_generate_crt0__mutmut_7 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_8'] = x_generate_crt0__mutmut_8 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_9'] = x_generate_crt0__mutmut_9 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_10'] = x_generate_crt0__mutmut_10 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_11'] = x_generate_crt0__mutmut_11 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_12'] = x_generate_crt0__mutmut_12 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_13'] = x_generate_crt0__mutmut_13 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_14'] = x_generate_crt0__mutmut_14 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_15'] = x_generate_crt0__mutmut_15 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_16'] = x_generate_crt0__mutmut_16 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_17'] = x_generate_crt0__mutmut_17 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_18'] = x_generate_crt0__mutmut_18 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_19'] = x_generate_crt0__mutmut_19 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_20'] = x_generate_crt0__mutmut_20 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_21'] = x_generate_crt0__mutmut_21 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_22'] = x_generate_crt0__mutmut_22 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_23'] = x_generate_crt0__mutmut_23 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_24'] = x_generate_crt0__mutmut_24 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_25'] = x_generate_crt0__mutmut_25 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_26'] = x_generate_crt0__mutmut_26 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_27'] = x_generate_crt0__mutmut_27 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_28'] = x_generate_crt0__mutmut_28 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_29'] = x_generate_crt0__mutmut_29 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_30'] = x_generate_crt0__mutmut_30 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_31'] = x_generate_crt0__mutmut_31 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_32'] = x_generate_crt0__mutmut_32 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_33'] = x_generate_crt0__mutmut_33 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_34'] = x_generate_crt0__mutmut_34 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_35'] = x_generate_crt0__mutmut_35 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_36'] = x_generate_crt0__mutmut_36 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_37'] = x_generate_crt0__mutmut_37 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_38'] = x_generate_crt0__mutmut_38 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_39'] = x_generate_crt0__mutmut_39 # type: ignore # mutmut generated
mutants_x_generate_crt0__mutmut['x_generate_crt0__mutmut_40'] = x_generate_crt0__mutmut_40 # type: ignore # mutmut generated
