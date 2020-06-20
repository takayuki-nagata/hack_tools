/*
 * Copyright (c) 2020 Takayuki Nagata All rights reserved.
 */

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "symbol_table.h"

typedef struct symbol_table_entry {
	char *symbol;
	uint16_t address;
	struct symbol_table_entry *next;
} symbol_table_entry;

symbol_table_entry *symtbl_list;

void symbol_table_open(void)
{
	int i;
	char symr[4];

	symbol_table_add_entry("SP"  , 0x0000);
	symbol_table_add_entry("LCL" , 0x0001);
	symbol_table_add_entry("ARG" , 0x0002);
	symbol_table_add_entry("THIS", 0x0003);
	symbol_table_add_entry("THAT", 0x0004);
	for (i = 0; i <= 15; i++) {
		sprintf(symr, "R%d", i);
		symbol_table_add_entry(symr, i);
	}
	symbol_table_add_entry("SCREEN", 0x4000);
	symbol_table_add_entry("KBD"   , 0x6000);
}

void symbol_table_close(void)
{
	symbol_table_entry *e, *tmp;
	e = symtbl_list;
	while (e) {
		tmp = e;
		e = e->next;
		free(tmp->symbol);
		free(tmp);
	}
}

void symbol_table_add_entry(const char *symbol, const uint16_t address)
{
	symbol_table_entry *new;

	new = malloc(sizeof(symbol_table_entry));
	new->symbol = malloc(sizeof(char)*(strlen(symbol)+1));

	strcpy(new->symbol, symbol);
	new->address = address;
	new->next = NULL;

	if (!symtbl_list) {
		symtbl_list = new;
	} else {
		new->next = symtbl_list;
		symtbl_list = new;
	}
}

uint16_t _symbol_table_get_address(const char *symbol)
{
	symbol_table_entry *e;
	e = symtbl_list;
	while (e) {
		if (!strcmp(e->symbol, symbol))
			return e->address;
		e = e->next;
	}
	return SYMTBL_ERROR;
}

bool symbol_table_contains(const char *symbol)
{
	if (SYMTBL_ERROR == _symbol_table_get_address(symbol))
		return false;
	return true;
}

uint16_t symbol_table_get_address(const char *symbol)
{
	return _symbol_table_get_address(symbol);
}
