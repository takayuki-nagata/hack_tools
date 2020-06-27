/*
 * Copyright (c) 2020 Takayuki Nagata All rights reserved.
 */

#ifndef _OUTPUT_FORMATTER_H
#define _OUTPUT_FORMATTER_H

#include <stdint.h>
#include <stdio.h>

typedef enum {
	HACK = 0,
	RAW,
	COE,
} output_format_type;

typedef struct {
	void (*header) (FILE *outfile);
	void (*body) (uint16_t binary, FILE *outfile);
	void (*footer) (FILE *outfile);
} output_formatter;

extern output_formatter* get_output_formatter(output_format_type type);

#endif /* _OUTPUT_FORMATTER_H */
