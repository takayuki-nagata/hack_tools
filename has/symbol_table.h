// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#ifndef HAS_SYMBOL_TABLE_H
#define HAS_SYMBOL_TABLE_H

#include <stdbool.h>
#include <stdint.h>

#define SYMTBL_ERROR ((uint16_t)0xffff)

void symbol_table_open(void);
void symbol_table_close(void);
bool symbol_table_add_entry(const char *symbol, uint16_t address);
bool symbol_table_contains(const char *symbol);
uint16_t symbol_table_get_address(const char *symbol);

#endif /* HAS_SYMBOL_TABLE_H */
