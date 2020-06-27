/*
 * Copyright (c) 2020 Takayuki Nagata All rights reserved.
 */

#include <stdint.h>
#include <stdio.h>
#include "output_formatter.h"

static void btoa(uint16_t binary, char *str)
{
	int i;
	for (i = 0; i < 16; i++) {
		str[i] = ((binary >> (15-i)) & 1) ? '1' : '0';
	}
	str[i] = '\0';
}


static void hack_body(uint16_t binary, FILE *outfile)
{
	char outstr[17];
	btoa(binary, outstr);
	fprintf(outfile, "%s\n", outstr);
}

output_formatter hack_formatter = {
	NULL,
	hack_body,
	NULL,
};

static void raw_body(uint16_t binary, FILE *outfile)
{
	char upper, lower;
	upper = (char)((binary & 0xff00) >> 8);
	lower = (char)(binary & 0x00ff);
	fputc(upper, outfile);
	fputc(lower, outfile);
}

output_formatter raw_formatter = {
	NULL,
	raw_body,
	NULL,
};

static void coe_header(FILE *outfile)
{
	fprintf(outfile, "memory_initialization_radix=16;\n");
	fprintf(outfile, "memory_initialization_vector=\n");
}

static void coe_body(uint16_t binary, FILE *outfile)
{
	fprintf(outfile, "%04x,\n", binary);
}

static void coe_footer(FILE *outfile)
{
	fprintf(outfile, ";");
}

output_formatter coe_formatter = {
	coe_header,
	coe_body,
	coe_footer,
};

output_formatter* get_output_formatter(output_format_type type)
{
	output_formatter *formatter;
	switch (type)
	{
	case HACK:
		formatter = &hack_formatter;
		break;
	case RAW:
		formatter = &raw_formatter;
		break;
	case COE:
		formatter = &coe_formatter;
		break;
	default:
		formatter = NULL;
	}
	return formatter;
}
