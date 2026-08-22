// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// All instructions comprehensive test for Hack Assembler

// A-instructions
@0
@1
@32767

// C-instructions: comp (a=0)
0
1
-1
D
A
!D
!A
-D
-A
D+1
A+1
D-1
A-1
D+A
D-A
A-D
D&A
D|A

// C-instructions: comp (a=1)
M
!M
-M
M+1
M-1
D+M
D-M
M-D
D&M
D|M

// C-instructions: dest
M=0
D=0
MD=0
A=0
AM=0
AD=0
AMD=0

// C-instructions: jump
0;JGT
0;JEQ
0;JGE
0;JLT
0;JNE
0;JLE
0;JMP

// Full C-instruction: dest=comp;jump
AMD=D+M;JMP
