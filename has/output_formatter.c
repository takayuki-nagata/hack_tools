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


static void hack_formatter(uint16_t binary, FILE *outfile)
{
	char outstr[17];
	btoa(binary, outstr);
	fprintf(outfile, "%s\n", outstr);
}

static void raw_formatter(uint16_t binary, FILE *outfile)
{
	char upper, lower;
	upper = (char)((binary & 0xff00) >> 8);
	lower = (char)(binary & 0x00ff);
	fputc(upper, outfile);
	fputc(lower, outfile);
}

output_formatter_t get_output_formatter(output_format_type type)
{
	output_formatter_t formatter;
	switch (type)
	{
	case HACK:
		formatter = hack_formatter;
		break;
	case RAW:
		formatter = raw_formatter;
		break;
	default:
		formatter = NULL;
	}
	return formatter;
}
