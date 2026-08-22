// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Multiplies R0 and R1 and stores the result in R2.

   @R2
   M=0
   @R1
   D=M
   @i
   M=D
(LOOP)
   @i
   D=M
   @END
   D;JEQ
   @R0
   D=M
   @R2
   M=D+M
   @i
   M=M-1
   @LOOP
   0;JMP
(END)
   @END
   0;JMP
