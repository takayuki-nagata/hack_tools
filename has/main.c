// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#include "assembler.h"
#include "output_formatter.h"
#include <getopt.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HAS_VERSION "0.2.0"

typedef struct {
    const char *infile_name;
    char *outfile_name;
    const output_formatter *formatter;
    output_format_type format_type;
    bool stdout_mode;
    bool allocated_outfile;
} options_t;

static void show_usage(FILE *stream) {
    fprintf(stream,
            "Usage: has [OPTION]... FILE\n"
            "Assemble Hack assembly (.asm) into machine code.\n\n"
            "Options:\n"
            "  -o, --outfile=FILE       Output to FILE.\n"
            "  -r, --raw                Use raw binary format (.bin).\n"
            "  -c, --coe                Use Xilinx COE format (.coe).\n"
            "  -s, --stdout             Output to stdout instead of a file.\n"
            "  -h, --help               Display this help text and exit.\n"
            "  -v, --version            Output version information and exit.\n\n"
            "Default output format is Hack text binary (.hack).\n");
}

static void show_version(void) {
    printf("has (hack_tools) version %s\n"
           "Copyright (c) 2020-2026 Takayuki Nagata\n"
           "License: MIT <https://opensource.org/licenses/MIT>\n",
           HAS_VERSION);
}

static char *create_outfile_name(const char *infile_name, const char *suffix) {
    size_t in_len = strlen(infile_name);
    size_t suf_len = strlen(suffix);

    const char *dot = strrchr(infile_name, '.');
    size_t base_len = dot ? (size_t)(dot - infile_name) : in_len;

    char *outfile_name = malloc(base_len + suf_len + 1);
    if (!outfile_name) {
        return NULL;
    }

    memcpy(outfile_name, infile_name, base_len);
    memcpy(outfile_name + base_len, suffix, suf_len + 1);

    return outfile_name;
}

static bool is_asm_file(const char *infile_name) {
    if (!infile_name) {
        return false;
    }
    const char *dot = strrchr(infile_name, '.');
    if (!dot) {
        return false;
    }
    return strcmp(dot, ".asm") == 0;
}

static bool parse_options(int argc, char *argv[], options_t *opts) {
    static const struct option long_options[] = {
        {"outfile", required_argument, NULL, 'o'},
        {"raw", no_argument, NULL, 'r'},
        {"coe", no_argument, NULL, 'c'},
        {"stdout", no_argument, NULL, 's'},
        {"help", no_argument, NULL, 'h'},
        {"version", no_argument, NULL, 'v'},
        {NULL, 0, NULL, 0},
    };

    opts->infile_name = NULL;
    opts->outfile_name = NULL;
    opts->formatter = NULL;
    opts->format_type = HACK;
    opts->stdout_mode = false;
    opts->allocated_outfile = false;

    int opt;
    while ((opt = getopt_long(argc, argv, "o:rcshv", long_options, NULL)) != -1) {
        switch (opt) {
        case 'o':
            opts->outfile_name = optarg;
            break;
        case 'r':
            opts->format_type = RAW;
            break;
        case 'c':
            opts->format_type = COE;
            break;
        case 's':
            opts->stdout_mode = true;
            break;
        case 'h':
            show_usage(stdout);
            exit(EXIT_SUCCESS);
        case 'v':
            show_version();
            exit(EXIT_SUCCESS);
        default:
            show_usage(stderr);
            return false;
        }
    }

    if (optind >= argc) {
        fprintf(stderr, "has: error: missing input file\n");
        show_usage(stderr);
        return false;
    }

    opts->infile_name = argv[optind];
    if (!is_asm_file(opts->infile_name)) {
        fprintf(stderr, "has: error: input file must have a .asm extension: '%s'\n",
                opts->infile_name);
        return false;
    }

    opts->formatter = get_output_formatter(opts->format_type);
    if (!opts->formatter) {
        fprintf(stderr, "has: error: invalid output formatter\n");
        return false;
    }

    const char *suffix = ".hack";
    if (opts->format_type == RAW) {
        suffix = ".bin";
    } else if (opts->format_type == COE) {
        suffix = ".coe";
    }

    if (!opts->stdout_mode && !opts->outfile_name) {
        opts->outfile_name = create_outfile_name(opts->infile_name, suffix);
        if (!opts->outfile_name) {
            fprintf(stderr, "has: error: failed to allocate memory for output filename\n");
            return false;
        }
        opts->allocated_outfile = true;
    }

    return true;
}

int main(int argc, char *argv[]) {
    options_t opts;
    if (!parse_options(argc, argv, &opts)) {
        return EXIT_FAILURE;
    }

    FILE *outfile = NULL;
    if (opts.stdout_mode) {
        outfile = stdout;
    } else {
        outfile = fopen(opts.outfile_name, "w");
        if (!outfile) {
            fprintf(stderr, "has: error: unable to open output file '%s'\n", opts.outfile_name);
            if (opts.allocated_outfile) {
                free(opts.outfile_name);
            }
            return EXIT_FAILURE;
        }
    }

    bool success = assembler(opts.infile_name, outfile, opts.formatter);

    if (outfile != stdout) {
        fclose(outfile);
        if (!success) {
            remove(opts.outfile_name);
        }
    }

    if (opts.allocated_outfile) {
        free(opts.outfile_name);
    }

    return success ? EXIT_SUCCESS : EXIT_FAILURE;
}
