/*
 * Copyright (c) 2020 Takayuki Nagata All rights reserved.
 */

#ifndef _ASSEMBLER_H
#define _ASSEMBLER_H

#include <stdio.h>
#include "output_formatter.h"

extern void assembler(char *infile_name, FILE *outfile, output_formatter_t formatter);

#endif /* _ASSEMBLER_H */
