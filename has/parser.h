// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#ifndef HAS_PARSER_H
#define HAS_PARSER_H

#include <stdbool.h>

typedef enum {
    A_COMMAND = 0,
    C_COMMAND,
    L_COMMAND,
    INVALID_COMMAND,
} command_type_t;

bool parser_open(const char *fpath);
void parser_close(void);
bool parser_has_more_commands(void);
bool parser_advanced(void);
command_type_t parser_command_type(void);
const char *parser_symbol(void);
const char *parser_dest(void);
const char *parser_comp(void);
const char *parser_jump(void);
int parser_get_line_number(void);

#endif /* HAS_PARSER_H */
