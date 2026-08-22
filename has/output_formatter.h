// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#ifndef HAS_OUTPUT_FORMATTER_H
#define HAS_OUTPUT_FORMATTER_H

#include <stdint.h>
#include <stdio.h>

typedef enum {
    HACK = 0,
    RAW,
    COE,
} output_format_type;

typedef struct {
    void (*header)(FILE *outfile);
    void (*body)(uint16_t binary, FILE *outfile);
    void (*footer)(FILE *outfile);
} output_formatter;

const output_formatter *get_output_formatter(output_format_type type);

#endif /* HAS_OUTPUT_FORMATTER_H */
