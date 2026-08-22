// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#include "assembler.h"
#include "code.h"
#include "output_formatter.h"
#include "parser.h"
#include "symbol_table.h"
#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>

#define VAR_ADDR_START ((uint16_t)0x0010)
#define PC_ADDR_START ((uint16_t)0x0000)

static bool is_numeric_value(const char *symbol) {
    if (!symbol || symbol[0] == '\0') {
        return false;
    }
    for (size_t i = 0; symbol[i] != '\0'; i++) {
        if (!isdigit((unsigned char)symbol[i])) {
            return false;
        }
    }
    return true;
}

static bool is_valid_symbol_char(char c, bool is_first) {
    if (isalpha((unsigned char)c) || c == '_' || c == '.' || c == '$' || c == ':') {
        return true;
    }
    if (!is_first && isdigit((unsigned char)c)) {
        return true;
    }
    return false;
}

static bool is_valid_symbol_name(const char *symbol) {
    if (!symbol || symbol[0] == '\0') {
        return false;
    }
    if (!is_valid_symbol_char(symbol[0], true)) {
        return false;
    }
    for (size_t i = 1; symbol[i] != '\0'; i++) {
        if (!is_valid_symbol_char(symbol[i], false)) {
            return false;
        }
    }
    return true;
}

static bool phase1(const char *infile_name) {
    uint16_t pc_addr = PC_ADDR_START;

    if (!parser_open(infile_name)) {
        return false;
    }

    while (parser_has_more_commands()) {
        if (!parser_advanced()) {
            break;
        }
        command_type_t type = parser_command_type();
        switch (type) {
        case A_COMMAND:
        case C_COMMAND:
            pc_addr++;
            break;
        case L_COMMAND: {
            const char *symbol = parser_symbol();
            if (!symbol || !is_valid_symbol_name(symbol)) {
                fprintf(stderr, "has: error (line %d): invalid label name '%s'\n",
                        parser_get_line_number(), symbol ? symbol : "(null)");
                parser_close();
                return false;
            }
            if (!symbol_table_add_entry(symbol, pc_addr)) {
                parser_close();
                return false;
            }
            break;
        }
        case INVALID_COMMAND:
        default:
            parser_close();
            return false;
        }
    }
    parser_close();
    return true;
}

static bool phase2(const char *infile_name, FILE *outfile, const output_formatter *formatter) {
    uint16_t var_addr = VAR_ADDR_START;

    if (!parser_open(infile_name)) {
        return false;
    }

    while (parser_has_more_commands()) {
        if (!parser_advanced()) {
            break;
        }
        command_type_t type = parser_command_type();
        uint16_t binary = 0;

        switch (type) {
        case A_COMMAND: {
            const char *symbol = parser_symbol();
            if (!symbol) {
                parser_close();
                return false;
            }

            if (is_numeric_value(symbol)) {
                long val = strtol(symbol, NULL, 10);
                if (val < 0 || val > 32767) {
                    fprintf(stderr,
                            "has: error (line %d): constant value '%s' exceeds 15-bit range "
                            "(0..32767)\n",
                            parser_get_line_number(), symbol);
                    parser_close();
                    return false;
                }
                binary = (uint16_t)val;
            } else if (symbol_table_contains(symbol)) {
                binary = symbol_table_get_address(symbol);
            } else if (is_valid_symbol_name(symbol)) {
                if (!symbol_table_add_entry(symbol, var_addr)) {
                    parser_close();
                    return false;
                }
                binary = var_addr;
                var_addr++;
            } else {
                fprintf(stderr, "has: error (line %d): invalid symbol name '%s'\n",
                        parser_get_line_number(), symbol);
                parser_close();
                return false;
            }
            break;
        }
        case C_COMMAND: {
            const char *dest_str = parser_dest();
            const char *comp_str = parser_comp();
            const char *jump_str = parser_jump();

            if (!comp_str) {
                parser_close();
                return false;
            }

            uint8_t dest_bin = code_dest(dest_str);
            uint8_t comp_bin = code_comp(comp_str);
            uint8_t jump_bin = code_jump(jump_str);

            if (dest_bin == CODE_ERROR || comp_bin == CODE_ERROR || jump_bin == CODE_ERROR) {
                parser_close();
                return false;
            }

            binary = CODE_COMPOSE(dest_bin, comp_bin, jump_bin);
            break;
        }
        case L_COMMAND:
            continue;

        case INVALID_COMMAND:
        default:
            parser_close();
            return false;
        }

        if (formatter && formatter->body) {
            formatter->body(binary, outfile);
        }
    }

    parser_close();
    return true;
}

bool assembler(const char *infile_name, FILE *outfile, const output_formatter *formatter) {
    if (!infile_name || !outfile || !formatter) {
        return false;
    }

    symbol_table_open();

    if (!phase1(infile_name)) {
        symbol_table_close();
        return false;
    }

    if (formatter->header) {
        formatter->header(outfile);
    }

    if (!phase2(infile_name, outfile, formatter)) {
        symbol_table_close();
        return false;
    }

    if (formatter->footer) {
        formatter->footer(outfile);
    }

    symbol_table_close();
    return true;
}
