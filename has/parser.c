// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#include "parser.h"
#include <ctype.h>
#include <stdio.h>
#include <string.h>

#define CMDMAX 1024
#define DESTSZ 16
#define JUMPSZ 16
#define COMPSZ 16
#define SYMBOLSZ 256

static FILE *source_fp = NULL;
static char current_command[CMDMAX];
static char dest[DESTSZ];
static char jump[JUMPSZ];
static char comp[COMPSZ];
static char symbol[SYMBOLSZ];
static int current_line_number = 0;
static bool has_peeked = false;
static bool at_eof = false;

static void parser_error(const char *msg) {
    if (current_command[0] != '\0') {
        fprintf(stderr, "has: error (line %d, '%s'): %s\n", current_line_number, current_command,
                msg);
    } else {
        fprintf(stderr, "has: error (line %d): %s\n", current_line_number, msg);
    }
}

bool parser_open(const char *fpath) {
    parser_close();
    if (!fpath) {
        fprintf(stderr, "has: error: failed to open source file '(null)'\n");
        return false;
    }
    source_fp = fopen(fpath, "r");
    if (!source_fp) {
        fprintf(stderr, "has: error: failed to open source file '%s'\n", fpath);
        return false;
    }
    current_line_number = 0;
    has_peeked = false;
    at_eof = false;
    current_command[0] = '\0';
    dest[0] = '\0';
    jump[0] = '\0';
    comp[0] = '\0';
    symbol[0] = '\0';
    return true;
}

void parser_close(void) {
    if (source_fp) {
        fclose(source_fp);
        source_fp = NULL;
    }
    has_peeked = false;
    at_eof = false;
}

int parser_get_line_number(void) {
    return current_line_number;
}

static bool fetch_next_command(char *out_buf, size_t buf_sz) {
    if (!source_fp || at_eof) {
        return false;
    }

    char line[1024];
    while (fgets(line, sizeof(line), source_fp) != NULL) {
        current_line_number++;

        // Strip comments starting with //
        char *comment_pos = strstr(line, "//");
        if (comment_pos) {
            *comment_pos = '\0';
        }

        // Strip whitespace
        size_t pos = 0;
        for (size_t i = 0; line[i] != '\0'; i++) {
            unsigned char c = (unsigned char)line[i];
            if (!isspace(c)) {
                if (pos + 1 < buf_sz) {
                    out_buf[pos++] = (char)c;
                }
            }
        }
        out_buf[pos] = '\0';

        if (pos > 0) {
            return true;
        }
    }

    at_eof = true;
    return false;
}

bool parser_has_more_commands(void) {
    if (!source_fp || at_eof) {
        return false;
    }
    if (has_peeked) {
        return true;
    }

    if (fetch_next_command(current_command, sizeof(current_command))) {
        has_peeked = true;
        return true;
    }
    return false;
}

bool parser_advanced(void) {
    dest[0] = '\0';
    comp[0] = '\0';
    jump[0] = '\0';
    symbol[0] = '\0';

    if (has_peeked) {
        has_peeked = false;
        return true;
    }

    return fetch_next_command(current_command, sizeof(current_command));
}

command_type_t parser_command_type(void) {
    if (current_command[0] == '@') {
        return A_COMMAND;
    } else if (current_command[0] == '(') {
        return L_COMMAND;
    } else if (current_command[0] != '\0') {
        return C_COMMAND;
    }
    return INVALID_COMMAND;
}

const char *parser_symbol(void) {
    symbol[0] = '\0';

    if (current_command[0] == '@') {
        size_t len = strlen(current_command) - 1;
        if (len == 0) {
            parser_error("empty A-instruction symbol");
            return NULL;
        }
        if (len >= sizeof(symbol)) {
            parser_error("symbol name exceeds maximum length");
            return NULL;
        }
        memcpy(symbol, &current_command[1], len);
        symbol[len] = '\0';
        return symbol;
    } else if (current_command[0] == '(') {
        const char *rparen = strchr(current_command, ')');
        if (!rparen) {
            parser_error("unclosed label declaration, missing ')'");
            return NULL;
        }
        size_t len = (size_t)(rparen - (current_command + 1));
        if (len == 0) {
            parser_error("empty label declaration '()'");
            return NULL;
        }
        if (len >= sizeof(symbol)) {
            parser_error("label name exceeds maximum length");
            return NULL;
        }
        memcpy(symbol, &current_command[1], len);
        symbol[len] = '\0';
        return symbol;
    }

    parser_error("parser_symbol called on non-symbol command");
    return NULL;
}

const char *parser_dest(void) {
    dest[0] = '\0';
    const char *eql = strchr(current_command, '=');
    if (eql) {
        size_t len = (size_t)(eql - current_command);
        if (len == 0 || len >= sizeof(dest)) {
            parser_error("invalid dest specification");
            return NULL;
        }
        memcpy(dest, current_command, len);
        dest[len] = '\0';
        return dest;
    }
    return NULL;
}

const char *parser_comp(void) {
    comp[0] = '\0';
    const char *start = current_command;
    const char *eql = strchr(current_command, '=');
    if (eql) {
        start = eql + 1;
    }

    const char *smc = strchr(start, ';');
    size_t len = smc ? (size_t)(smc - start) : strlen(start);

    if (len == 0 || len >= sizeof(comp)) {
        parser_error("invalid comp specification");
        return NULL;
    }

    memcpy(comp, start, len);
    comp[len] = '\0';
    return comp;
}

const char *parser_jump(void) {
    jump[0] = '\0';
    const char *smc = strchr(current_command, ';');
    if (smc) {
        const char *start = smc + 1;
        size_t len = strlen(start);
        if (len == 0 || len >= sizeof(jump)) {
            parser_error("invalid jump specification");
            return NULL;
        }
        memcpy(jump, start, len);
        jump[len] = '\0';
        return jump;
    }
    return NULL;
}
