/*
 * Copyright (c) 2020 Takayuki Nagata All rights reserved.
 */

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include "assembler.h"
#include "parser.h"
#include "code.h"
#include "symbol_table.h"
#include "output_formatter.h"

#define VAR_ADDR_START ((uint16_t)0x0010)
#define PC_ADDR_START  ((uint16_t)0x0000)

static bool is_symbol_value(char *symbol)
{
	if ('0' <= symbol[0] && symbol[0] <= '9')
		return true;
	else
		return false;
}

void phase1(char *infile_name)
{
	char *symbol;
	uint16_t var_addr = VAR_ADDR_START;
	uint16_t pc_addr = PC_ADDR_START;

	parser_open(infile_name);
	while (parser_has_more_commands()) {
		parser_advanced();
		switch (parser_command_type())
		{
		case A_COMMAND:
			pc_addr++;
			break;
		case C_COMMAND:
			pc_addr++;
			break;
		case L_COMMAND:
			symbol = parser_symbol();
			symbol_table_add_entry(symbol, pc_addr);
			break;
		}
	}
	parser_close();
}

void phase2(char *infile_name, FILE *outfile, output_formatter *formatter)
{
	char *comp_str, *dest_str, *jump_str, *symbol;
	uint16_t comp_bin, dest_bin, jump_bin;
	uint16_t binary;
	char binstr[17];

	uint16_t var_addr = VAR_ADDR_START;

	parser_open(infile_name);
	while (parser_has_more_commands()) {
		parser_advanced();
		switch (parser_command_type())
		{
		case A_COMMAND:
			symbol = parser_symbol();
			if (is_symbol_value(symbol))
				binary = atoi(symbol);
			else if (symbol_table_contains(symbol))
				binary = symbol_table_get_address(symbol);
			else {
				symbol_table_add_entry(symbol, var_addr);
				binary = var_addr;
				var_addr++;
			}
			break;
		case C_COMMAND:
			dest_str = parser_dest();
			comp_str = parser_comp();
			jump_str = parser_jump();
			dest_bin = code_dest(dest_str);
			comp_bin = code_comp(comp_str);
			jump_bin = code_jump(jump_str);
			binary = CODE_COMPOSE(dest_bin, comp_bin, jump_bin);
			break;
		case L_COMMAND:
			continue;
		}
		formatter->body(binary, outfile);
	}
	parser_close();
}

void assembler(char *infile_name, FILE *outfile, output_formatter *formatter)
{
	if (formatter->header)
		formatter->header(outfile);

	symbol_table_open();
	phase1(infile_name);
	phase2(infile_name, outfile, formatter);
	symbol_table_close();

	if (formatter->footer)
		formatter->footer(outfile);
}
