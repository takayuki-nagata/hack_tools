// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#include "output_formatter.h"
#include <stdint.h>
#include <stdio.h>

static void btoa(uint16_t binary, char *str) {
    for (int i = 0; i < 16; i++) {
        str[i] = ((binary >> (15 - i)) & 1) ? '1' : '0';
    }
    str[16] = '\0';
}

static void hack_body(uint16_t binary, FILE *outfile) {
    char outstr[17];
    btoa(binary, outstr);
    fprintf(outfile, "%s\n", outstr);
}

static const output_formatter hack_formatter = {
    NULL,
    hack_body,
    NULL,
};

static void raw_body(uint16_t binary, FILE *outfile) {
    unsigned char upper = (unsigned char)((binary >> 8) & 0xff);
    unsigned char lower = (unsigned char)(binary & 0xff);
    fputc(upper, outfile);
    fputc(lower, outfile);
}

static const output_formatter raw_formatter = {
    NULL,
    raw_body,
    NULL,
};

static void coe_header(FILE *outfile) {
    fprintf(outfile, "memory_initialization_radix=16;\n");
    fprintf(outfile, "memory_initialization_vector=\n");
}

static void coe_body(uint16_t binary, FILE *outfile) {
    fprintf(outfile, "%04x,\n", binary);
}

static void coe_footer(FILE *outfile) {
    fprintf(outfile, ";\n");
}

static const output_formatter coe_formatter = {
    coe_header,
    coe_body,
    coe_footer,
};

const output_formatter *get_output_formatter(output_format_type type) {
    switch (type) {
    case HACK:
        return &hack_formatter;
    case RAW:
        return &raw_formatter;
    case COE:
        return &coe_formatter;
    default:
        return NULL;
    }
}
