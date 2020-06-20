/*
 * Copyright (c) 2020 Takayuki Nagata All rights reserved.
 */

#ifndef _OUTPUT_FORMATTER_H
#define _OUTPUT_FORMATTER_H

#include <stdint.h>
#include <stdio.h>

typedef enum {
	HACK = 0,
	RAW
} output_format_type;

typedef void (*output_formatter_t)(uint16_t binary, FILE *outfile);
extern output_formatter_t get_output_formatter(output_format_type type);

#endif /* _OUTPUT_FORMATTER_H */
