// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#include "code.h"
#include <stdio.h>
#include <string.h>

#define CA 0x40
#define C1 0x20
#define C2 0x10
#define C3 0x08
#define C4 0x04
#define C5 0x02
#define C6 0x01

#define D1 0x04
#define D2 0x02
#define D3 0x01

#define J1 0x04
#define J2 0x02
#define J3 0x01

typedef struct {
    const char *mnemonic;
    uint8_t binary;
} instruction_table_t;

static const instruction_table_t comp_tbl0[] = {
    {"0", C1 | C3 | C5},
    {"1", C1 | C2 | C3 | C4 | C5 | C6},
    {"-1", C1 | C2 | C3 | C5},
    {"D", C3 | C4},
    {"A", C1 | C2},
    {"!D", C3 | C4 | C6},
    {"!A", C1 | C2 | C6},
    {"-D", C3 | C4 | C5 | C6},
    {"-A", C1 | C2 | C5 | C6},
    {"D+1", C2 | C3 | C4 | C5 | C6},
    {"A+1", C1 | C2 | C4 | C5 | C6},
    {"D-1", C3 | C4 | C5},
    {"A-1", C1 | C2 | C5},
    {"D+A", C5},
    {"D-A", C2 | C5 | C6},
    {"A-D", C4 | C5 | C6},
    {"D&A", 0},
    {"D|A", C2 | C4 | C6},
    {NULL, 0},
};

static const instruction_table_t comp_tbl1[] = {
    {"M", C1 | C2},
    {"!M", C1 | C2 | C6},
    {"-M", C1 | C2 | C5 | C6},
    {"M+1", C1 | C2 | C4 | C5 | C6},
    {"M-1", C1 | C2 | C5},
    {"D+M", C5},
    {"D-M", C2 | C5 | C6},
    {"M-D", C4 | C5 | C6},
    {"D&M", 0},
    {"D|M", C2 | C4 | C6},
    {NULL, 0},
};

static const instruction_table_t dest_tbl[] = {
    {"M", D3},       {"D", D2},       {"MD", D2 | D3},       {"A", D1},
    {"AM", D1 | D3}, {"AD", D1 | D2}, {"AMD", D1 | D2 | D3}, {NULL, 0},
};

static const instruction_table_t jump_tbl[] = {
    {"JGT", J3},      {"JEQ", J2},      {"JGE", J2 | J3},      {"JLT", J1},
    {"JNE", J1 | J3}, {"JLE", J1 | J2}, {"JMP", J1 | J2 | J3}, {NULL, 0},
};

static uint8_t search_tbl(const instruction_table_t *tbl, const char *mnemonic) {
    for (int i = 0; tbl[i].mnemonic != NULL; i++) {
        if (strcmp(mnemonic, tbl[i].mnemonic) == 0) {
            return tbl[i].binary;
        }
    }
    return CODE_ERROR;
}

uint8_t code_dest(const char *mnemonic) {
    if (!mnemonic || mnemonic[0] == '\0') {
        return 0x00;
    }
    uint8_t binary = search_tbl(dest_tbl, mnemonic);
    if (binary == CODE_ERROR) {
        fprintf(stderr, "has: error: invalid dest mnemonic '%s'\n", mnemonic);
    }
    return binary;
}

uint8_t code_comp(const char *mnemonic) {
    if (!mnemonic || mnemonic[0] == '\0') {
        fprintf(stderr, "has: error: missing comp mnemonic\n");
        return CODE_ERROR;
    }

    uint8_t binary = search_tbl(comp_tbl1, mnemonic);
    if (binary != CODE_ERROR) {
        return (uint8_t)(binary | CA);
    }

    binary = search_tbl(comp_tbl0, mnemonic);
    if (binary != CODE_ERROR) {
        return binary;
    }

    fprintf(stderr, "has: error: invalid comp mnemonic '%s'\n", mnemonic);
    return CODE_ERROR;
}

uint8_t code_jump(const char *mnemonic) {
    if (!mnemonic || mnemonic[0] == '\0') {
        return 0x00;
    }
    uint8_t binary = search_tbl(jump_tbl, mnemonic);
    if (binary == CODE_ERROR) {
        fprintf(stderr, "has: error: invalid jump mnemonic '%s'\n", mnemonic);
    }
    return binary;
}
