// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#include "../has/assembler.h"
#include "../has/code.h"
#include "../has/output_formatter.h"
#include "../has/parser.h"
#include "../has/symbol_table.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int total_asserts = 0;

#define TEST_ASSERT(cond)                                                                         \
    do {                                                                                          \
        total_asserts++;                                                                          \
        if (!(cond)) {                                                                            \
            fprintf(stderr, "Assertion failed: %s at %s:%d\n", #cond, __FILE__, __LINE__);        \
            exit(EXIT_FAILURE);                                                                   \
        }                                                                                         \
    } while (0)

static void test_symbol_table_edge_cases(void) {
    symbol_table_open();

    // Predefined symbols
    TEST_ASSERT(symbol_table_contains("SP"));
    TEST_ASSERT(symbol_table_get_address("SP") == 0x0000);
    TEST_ASSERT(symbol_table_contains("R15"));
    TEST_ASSERT(symbol_table_get_address("R15") == 15);
    TEST_ASSERT(symbol_table_contains("SCREEN"));
    TEST_ASSERT(symbol_table_get_address("SCREEN") == 0x4000);
    TEST_ASSERT(symbol_table_contains("KBD"));
    TEST_ASSERT(symbol_table_get_address("KBD") == 0x6000);

    // Nonexistent
    TEST_ASSERT(!symbol_table_contains("NON_EXISTENT"));
    TEST_ASSERT(symbol_table_get_address("NON_EXISTENT") == SYMTBL_ERROR);

    // NULL inputs
    TEST_ASSERT(!symbol_table_add_entry(NULL, 100));
    TEST_ASSERT(symbol_table_get_address(NULL) == SYMTBL_ERROR);
    TEST_ASSERT(!symbol_table_contains(NULL));

    // Add custom entry
    TEST_ASSERT(symbol_table_add_entry("custom_symbol", 0x1234));
    TEST_ASSERT(symbol_table_contains("custom_symbol"));
    TEST_ASSERT(symbol_table_get_address("custom_symbol") == 0x1234);

    // Close and reopen
    symbol_table_close();
    TEST_ASSERT(!symbol_table_contains("custom_symbol"));

    symbol_table_open();
    TEST_ASSERT(symbol_table_contains("SP"));
    symbol_table_close();
}

static void test_output_formatter_edge_cases(void) {
    TEST_ASSERT(get_output_formatter(HACK) != NULL);
    TEST_ASSERT(get_output_formatter(RAW) != NULL);
    TEST_ASSERT(get_output_formatter(COE) != NULL);
    TEST_ASSERT(get_output_formatter((output_format_type)999) == NULL);

    const output_formatter *coe = get_output_formatter(COE);
    TEST_ASSERT(coe->header != NULL);
    TEST_ASSERT(coe->body != NULL);
    TEST_ASSERT(coe->footer != NULL);
}

static void test_code_edge_cases(void) {
    // dest
    TEST_ASSERT(code_dest(NULL) == 0);
    TEST_ASSERT(code_dest("") == 0);
    TEST_ASSERT(code_dest("M") == 1);
    TEST_ASSERT(code_dest("AMD") == 7);
    TEST_ASSERT(code_dest("INVALID") == CODE_ERROR);

    // comp
    TEST_ASSERT(code_comp(NULL) == CODE_ERROR);
    TEST_ASSERT(code_comp("") == CODE_ERROR);
    TEST_ASSERT(code_comp("0") == 0x2a);
    TEST_ASSERT(code_comp("M") == (0x30 | 0x40));
    TEST_ASSERT(code_comp("INVALID") == CODE_ERROR);

    // jump
    TEST_ASSERT(code_jump(NULL) == 0);
    TEST_ASSERT(code_jump("") == 0);
    TEST_ASSERT(code_jump("JGT") == 1);
    TEST_ASSERT(code_jump("JMP") == 7);
    TEST_ASSERT(code_jump("INVALID") == CODE_ERROR);
}

static void test_parser_edge_cases(void) {
    TEST_ASSERT(!parser_open(NULL));
    TEST_ASSERT(!parser_open("/non/existent/path/file.asm"));

    // Operations when closed
    parser_close();
    TEST_ASSERT(!parser_has_more_commands());
    TEST_ASSERT(parser_command_type() == INVALID_COMMAND);
    TEST_ASSERT(parser_get_line_number() == 0);

    const char *temp_file = "test_out/unit_parser_temp.asm";
    FILE *fp = fopen(temp_file, "w");
    TEST_ASSERT(fp != NULL);

    // Empty A-instruction
    fprintf(fp, "@\n");

    // Empty label
    fprintf(fp, "()\n");

    // Unclosed label
    fprintf(fp, "(UNCLOSED\n");

    // Long symbol (>= 256 bytes)
    fprintf(fp, "@");
    for (int i = 0; i < 300; i++) {
        fputc('a', fp);
    }
    fprintf(fp, "\n");

    // Long label (>= 256 bytes)
    fprintf(fp, "(");
    for (int i = 0; i < 300; i++) {
        fputc('b', fp);
    }
    fprintf(fp, ")\n");

    // Invalid dest (=D)
    fprintf(fp, "=D\n");

    // Long dest (>= 16 bytes)
    fprintf(fp, "ABCDEFGHIJKLMN12345=D\n");

    // Invalid comp (D=)
    fprintf(fp, "D=\n");

    // Long comp (>= 16 bytes)
    fprintf(fp, "D=TOOLONGCOMPMNEMONICHERE\n");

    // Invalid jump (D;)
    fprintf(fp, "D;\n");

    // Long jump (>= 16 bytes)
    fprintf(fp, "D;TOOLONGJUMPNAMEHERE\n");

    // Valid command for testing direct advance & parser_symbol on non-symbol
    fprintf(fp, "D=A\n");

    fclose(fp);

    TEST_ASSERT(parser_open(temp_file));

    // 1. Empty A-instruction
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_has_more_commands()); // Test peek idempotent
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == A_COMMAND);
    TEST_ASSERT(parser_symbol() == NULL);

    // 2. Empty label
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == L_COMMAND);
    TEST_ASSERT(parser_symbol() == NULL);

    // 3. Unclosed label
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == L_COMMAND);
    TEST_ASSERT(parser_symbol() == NULL);

    // 4. Long symbol
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == A_COMMAND);
    TEST_ASSERT(parser_symbol() == NULL);

    // 5. Long label
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == L_COMMAND);
    TEST_ASSERT(parser_symbol() == NULL);

    // 6. Invalid dest (=D)
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == C_COMMAND);
    TEST_ASSERT(parser_dest() == NULL);

    // 7. Long dest
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == C_COMMAND);
    TEST_ASSERT(parser_dest() == NULL);

    // 8. Invalid comp (D=)
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == C_COMMAND);
    TEST_ASSERT(parser_comp() == NULL);

    // 9. Long comp
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == C_COMMAND);
    TEST_ASSERT(parser_comp() == NULL);

    // 10. Invalid jump (D;)
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == C_COMMAND);
    TEST_ASSERT(parser_jump() == NULL);

    // 11. Long jump
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == C_COMMAND);
    TEST_ASSERT(parser_jump() == NULL);

    // 12. Valid C command: test parser_symbol on C command
    TEST_ASSERT(parser_has_more_commands());
    TEST_ASSERT(parser_advanced());
    TEST_ASSERT(parser_command_type() == C_COMMAND);
    TEST_ASSERT(parser_symbol() == NULL);
    TEST_ASSERT(strcmp(parser_dest(), "D") == 0);
    TEST_ASSERT(strcmp(parser_comp(), "A") == 0);
    TEST_ASSERT(parser_jump() == NULL);

    // Direct advance without peek (at EOF)
    TEST_ASSERT(!parser_advanced());
    TEST_ASSERT(!parser_has_more_commands());

    parser_close();
    remove(temp_file);
}

static void test_assembler_edge_cases(void) {
    const output_formatter *fmt = get_output_formatter(HACK);
    TEST_ASSERT(!assembler(NULL, stdout, fmt));
    TEST_ASSERT(!assembler("nonexistent.asm", NULL, fmt));
    TEST_ASSERT(!assembler("nonexistent.asm", stdout, NULL));

    // Phase 1 error: invalid label in asm file
    const char *bad_label_file = "test_out/bad_label_unit.asm";
    FILE *fp = fopen(bad_label_file, "w");
    TEST_ASSERT(fp != NULL);
    fprintf(fp, "(1INVALID_LABEL)\n");
    fclose(fp);
    TEST_ASSERT(!assembler(bad_label_file, stdout, fmt));
    remove(bad_label_file);

    // Phase 1 error: unclosed label
    fp = fopen(bad_label_file, "w");
    TEST_ASSERT(fp != NULL);
    fprintf(fp, "(UNCLOSED_LABEL\n");
    fclose(fp);
    TEST_ASSERT(!assembler(bad_label_file, stdout, fmt));
    remove(bad_label_file);

    // Phase 2 error: invalid symbol in asm file
    const char *bad_sym_file = "test_out/bad_sym_unit.asm";
    fp = fopen(bad_sym_file, "w");
    TEST_ASSERT(fp != NULL);
    fprintf(fp, "@1INVALID\n");
    fclose(fp);
    TEST_ASSERT(!assembler(bad_sym_file, stdout, fmt));
    remove(bad_sym_file);

    // Phase 2 error: invalid symbol with invalid char in body
    fp = fopen(bad_sym_file, "w");
    TEST_ASSERT(fp != NULL);
    fprintf(fp, "@VAR#INVALID\n");
    fclose(fp);
    TEST_ASSERT(!assembler(bad_sym_file, stdout, fmt));
    remove(bad_sym_file);

    // Phase 2 error: empty symbol
    fp = fopen(bad_sym_file, "w");
    TEST_ASSERT(fp != NULL);
    fprintf(fp, "@\n");
    fclose(fp);
    TEST_ASSERT(!assembler(bad_sym_file, stdout, fmt));
    remove(bad_sym_file);

    // Phase 2 error: invalid comp mnemonic in C command
    const char *bad_c_file = "test_out/bad_c_unit.asm";
    fp = fopen(bad_c_file, "w");
    TEST_ASSERT(fp != NULL);
    fprintf(fp, "D=INVALID\n");
    fclose(fp);
    TEST_ASSERT(!assembler(bad_c_file, stdout, fmt));
    remove(bad_c_file);

    // Phase 2 error: invalid dest mnemonic in C command
    fp = fopen(bad_c_file, "w");
    TEST_ASSERT(fp != NULL);
    fprintf(fp, "BADDEST=D\n");
    fclose(fp);
    TEST_ASSERT(!assembler(bad_c_file, stdout, fmt));
    remove(bad_c_file);

    // Phase 2 error: invalid jump mnemonic in C command
    fp = fopen(bad_c_file, "w");
    TEST_ASSERT(fp != NULL);
    fprintf(fp, "0;BADJUMP\n");
    fclose(fp);
    TEST_ASSERT(!assembler(bad_c_file, stdout, fmt));
    remove(bad_c_file);

    // Phase 2 error: missing comp
    fp = fopen(bad_c_file, "w");
    TEST_ASSERT(fp != NULL);
    fprintf(fp, "D=\n");
    fclose(fp);
    TEST_ASSERT(!assembler(bad_c_file, stdout, fmt));
    remove(bad_c_file);
}

int main(void) {
    printf("Running C Unit Tests...\n");
    test_symbol_table_edge_cases();
    test_output_formatter_edge_cases();
    test_code_edge_cases();
    test_parser_edge_cases();
    test_assembler_edge_cases();
    printf("Unit tests completed successfully (%d assertions passed).\n", total_asserts);
    return 0;
}
