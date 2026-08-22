// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Symbols and labels test for Hack Assembler

// Predefined symbols
@SP
@LCL
@ARG
@THIS
@THAT
@R0
@R1
@R2
@R3
@R4
@R5
@R6
@R7
@R8
@R9
@R10
@R11
@R12
@R13
@R14
@R15
@SCREEN
@KBD

// Labels and variables
(START)
@var1
M=1
@var2
M=0
@END
0;JMP
@START
(END)
@var1
D=M
