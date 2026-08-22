// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Edge cases: comments, trailing spaces, tabs, empty lines, CRLF

   
// Full line comment
   // Indented comment
@32767	   // A-instruction with trailing spaces & tabs
	D=A	   // Tab indentation
(MY_LABEL_1)
//
@MY_LABEL_1  // Label reference
0;JMP // Jump
