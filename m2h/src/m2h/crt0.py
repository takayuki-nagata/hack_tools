# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

"""Runtime startup code generator (crt0) for Hack programs."""


def generate_crt0(stack_start: int = 16384, entry_point: str = "main") -> list[str]:
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
        "M=M-1",
        "A=M",
        "M=D",
        f"@{entry_point}",
        "0;JMP",
        "(__HALT)",
        "@__HALT",
        "0;JMP",
        "// === End of Startup ===",
    ]
