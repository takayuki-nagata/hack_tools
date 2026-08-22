// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#include "symbol_table.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct symbol_table_entry {
    char *symbol;
    uint16_t address;
    struct symbol_table_entry *next;
} symbol_table_entry;

static symbol_table_entry *symtbl_list = NULL;

bool symbol_table_add_entry(const char *symbol, const uint16_t address) {
    if (!symbol) {
        return false;
    }

    symbol_table_entry *new_entry = malloc(sizeof(symbol_table_entry));
    if (!new_entry) {
        return false;
    }

    size_t len = strlen(symbol);
    new_entry->symbol = malloc(len + 1);
    if (!new_entry->symbol) {
        free(new_entry);
        return false;
    }

    memcpy(new_entry->symbol, symbol, len + 1);
    new_entry->address = address;
    new_entry->next = symtbl_list;
    symtbl_list = new_entry;

    return true;
}

void symbol_table_open(void) {
    symbol_table_close();

    symbol_table_add_entry("SP", 0x0000);
    symbol_table_add_entry("LCL", 0x0001);
    symbol_table_add_entry("ARG", 0x0002);
    symbol_table_add_entry("THIS", 0x0003);
    symbol_table_add_entry("THAT", 0x0004);

    char symr[16];
    for (int i = 0; i <= 15; i++) {
        snprintf(symr, sizeof(symr), "R%d", i);
        symbol_table_add_entry(symr, (uint16_t)i);
    }

    symbol_table_add_entry("SCREEN", 0x4000);
    symbol_table_add_entry("KBD", 0x6000);
}

void symbol_table_close(void) {
    symbol_table_entry *e = symtbl_list;
    while (e) {
        symbol_table_entry *tmp = e;
        e = e->next;
        free(tmp->symbol);
        free(tmp);
    }
    symtbl_list = NULL;
}

uint16_t symbol_table_get_address(const char *symbol) {
    if (!symbol) {
        return SYMTBL_ERROR;
    }

    symbol_table_entry *e = symtbl_list;
    while (e) {
        if (strcmp(e->symbol, symbol) == 0) {
            return e->address;
        }
        e = e->next;
    }
    return SYMTBL_ERROR;
}

bool symbol_table_contains(const char *symbol) {
    return symbol_table_get_address(symbol) != SYMTBL_ERROR;
}
