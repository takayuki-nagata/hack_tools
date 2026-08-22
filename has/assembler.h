// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#ifndef HAS_ASSEMBLER_H
#define HAS_ASSEMBLER_H

#include "output_formatter.h"
#include <stdbool.h>
#include <stdio.h>

bool assembler(const char *infile_name, FILE *outfile, const output_formatter *formatter);

#endif /* HAS_ASSEMBLER_H */
