/*
 * Copyright (c) 2020 Takayuki Nagata All rights reserved.
 */

#include <stdio.h>
#include <string.h>
#include "parser.h"

#ifdef DEBUG
#define PARSER_ADVANCED_DEBUG(c) (printf("%c", c));
#else
#define PARSER_ADVANCED_DEBUG(c)
#endif

#define CMDMAX 256
#define DESTSZ 4
#define JUMPSZ 4
#define COMPSZ 4
#define SYMBOLSZ 125

FILE *source_fp = NULL;
char current_command[CMDMAX];
char dest[DESTSZ];
char jump[JUMPSZ];
char comp[COMPSZ];
char symbol[SYMBOLSZ];

static void parser_error(const char *msg)
{
	printf("parser error: %s: %s\n", current_command, msg);
}


void parser_open(const char *fpath)
{
	if ((source_fp = fopen(fpath, "r"))) {
		memset(current_command, 0, CMDMAX);
		memset(dest, 0, DESTSZ);
		memset(comp, 0, COMPSZ);
		memset(symbol, 0, SYMBOLSZ);
	} else {
		parser_error("failed to open source file");
	}
}

void parser_close(void)
{
	if (source_fp) {
		fclose(source_fp);
		source_fp = NULL;
	}
}

bool parser_has_more_commands(void)
{
	char c;
	if (source_fp) {
		c = fgetc(source_fp);
		if (EOF == c) {
			return false;
		} else if ('\n' != c) {
			fseek(source_fp, -1, SEEK_CUR);
			return true;
		}
	}
	return false;
}

void parser_advanced(void)
{
	char p = '\0', c;
	bool comment = false;
	int pos = 0;

	while ((c = fgetc(source_fp)) != EOF) {
		PARSER_ADVANCED_DEBUG(c);
		if (comment) {
			if('\n' == c) {
				if (pos)
					return;
				comment = false;
			}
			continue;
		} else {
			if ('/' == p && '/' == c) {
				comment = true;
				if (pos)
					current_command[--pos] = '\0';
				continue;
			}
			if (' ' == c || '\r' == c)
				continue;
			if ('\n' == c) {
				if (pos) {
					current_command[pos] = '\0';
					return;
				} else {
					pos = 0;
					continue;
				}
			}
			current_command[pos++] = c;
		}
		p = c;
	}
}

int parser_command_type(void)
{
	switch (current_command[0])
	{
	case '@':
		return A_COMMAND;
	case '(':
		return L_COMMAND;
	default:
		return C_COMMAND;
	}
}

char* parser_symbol(void)
{
	int rparpos, symlen;

	memset(symbol, 0, SYMBOLSZ);

	switch (current_command[0])
	{
	case '@':
		symlen = strlen(current_command) - 1;
		break;
	case '(':
		rparpos = strchr(current_command, ')') - current_command;
		symlen = rparpos - 1;
		break;
	}

	if (symlen <= SYMBOLSZ) {
		strncpy(symbol, &current_command[1], symlen);
		return symbol;
	} else {
		parser_error("too long value");
	}

	return NULL;
}

char* parser_dest(void)
{
	int eqlpos, destlen;

	memset(dest, 0, DESTSZ);
	eqlpos = strchr(current_command, '=') - current_command;

	if (eqlpos >= 0) {
		destlen = eqlpos;
		if (destlen <= 3) {
			strncpy(dest, current_command, destlen);
			return dest;
		} else {
			parser_error("invalid dest command");
			return NULL;
		}
	}
	return NULL;
}

char* parser_comp(void)
{
	int eqlpos, smcpos, complen;

	memset(comp, 0, COMPSZ);
	eqlpos = strchr(current_command, '=') - current_command;
	smcpos = strchr(current_command, ';') - current_command;

	if (eqlpos >= 0) {
		if (smcpos >= 0)
			complen = smcpos - eqlpos;
		else
			complen = strlen(current_command) - (eqlpos + 1);

		if (complen > 0 && complen <= 3) {
			strncpy(comp, &current_command[eqlpos+1], complen);
			return comp;
		} else {
			parser_error("invalid comp command");
		}
	} else {
		if (smcpos >= 0)
			complen = smcpos;
		else
			complen = strlen(current_command);

		if (complen <= 3) {
			strncpy(comp, current_command, complen);
			return comp;
		} else {
			parser_error("invalid comp command");
		}
	}
	return NULL;
}

char* parser_jump(void)
{
	int smcpos, jumplen;

	memset(jump, 0, JUMPSZ);
	smcpos = strchr(current_command, ';') - current_command;

	if (smcpos >= 0) {
		jumplen = strlen(current_command) - (smcpos + 1);
		if (jumplen == 3) {
			strncpy(jump, &current_command[smcpos+1], jumplen);
			return jump;
		} else {
			parser_error("illegal jump command");
		}
	}
	return NULL;
}

