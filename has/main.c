/*
 * Copyright (c) 2020 Takayuki Nagata All rights reserved.
 */

#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <string.h>
#include <stdbool.h>
#include "assembler.h"
#include "output_formatter.h"

char *opt_infile_name;
char *opt_outfile_name;
output_formatter_t opt_formatter;
bool opt_stdout;

void show_usage(void)
{
	fprintf(stderr,
		"Usage: has [OPTION]... FILE\n"
		"  -o, --outfile=FILE       output to FILE.\n"
		"  -r, --raw                use raw binary format.\n"
		"  -s, --stdout             output fo stdout instead of file.\n"
		);
}

void create_outfile_name(const char *infile_name, char *suffix, char **poutfile_name)
{
	char *outfile_name, *outfile_suffix_pos;

	/* get file name from file path */
	if (strchr(infile_name, '/')) {
		outfile_name = malloc(strlen(strchr(infile_name, '/'))+strlen(suffix));
		strcpy(outfile_name, (strchr(infile_name, '/')+1));
	} else {
		outfile_name = malloc(strlen(infile_name)+strlen(suffix));
		strcpy(outfile_name, infile_name);
	}

	/* replace or add suffix */
	outfile_suffix_pos = strrchr(outfile_name, '.');
	if (outfile_suffix_pos)
		strcpy(outfile_suffix_pos, suffix);
	else
		strcat(outfile_name, suffix);

	*poutfile_name = outfile_name;
}

void destroy_outfile_name(char *outfile_name)
{
	free(outfile_name);
}

bool is_asm_file(const char *infile_name)
{
	char *infile_suffix_pos;

	infile_suffix_pos = strrchr(infile_name, '.');
	if (!infile_suffix_pos)
		return false;
	if (strcmp(infile_suffix_pos, ".asm"))
		return false;
	return true;
}

void set_options(int argc, char*argv[])
{
	int opt;
	char outfile_suffix[10];
	static struct option long_options[] = {
		{"outfile", required_argument, 0, 'o'},
		{"raw",    required_argument, 0, 'r'},
		{"stdout", no_argument,       0, 's'},
		{0, 0, 0, 0},
	};

	while ((opt = getopt_long(argc, argv, "or",
					long_options, NULL)) != -1) {
		switch (opt) {
		case 'o':
			opt_outfile_name = optarg;
			break;
		case 'r':
			opt_formatter = get_output_formatter(RAW);
			strcpy(outfile_suffix, ".bin");
			break;
		case 's':
			opt_stdout = true;
			break;
		default:
			show_usage();
			exit(EXIT_FAILURE);
		}
	}

	if (optind >= argc) {
		show_usage();
		exit(EXIT_FAILURE);
	}

	opt_infile_name = argv[optind];
	if (!is_asm_file(opt_infile_name)) {
		fprintf(stderr, "input file should be .asm\n");
		exit(EXIT_FAILURE);
	}

	if (!opt_formatter) {
		/* default: HACK format with .hack suffix */
		opt_formatter = get_output_formatter(HACK);
		strcpy(outfile_suffix, ".hack");
	}

	if (!opt_outfile_name) {
		/* default: <infile>.<suffix> */
		create_outfile_name(opt_infile_name, outfile_suffix, &opt_outfile_name);
	}
}

int main(int argc, char *argv[])
{
	FILE *outfile;

	set_options(argc, argv);

	if (opt_stdout) {
		outfile = stdout;
	} else if (!(outfile = fopen(opt_outfile_name, "w"))){
		fprintf(stderr, "unable to open file: %s\n", opt_outfile_name);
		exit(EXIT_FAILURE);
	}

	assembler(opt_infile_name, outfile, opt_formatter);

	fclose(outfile);
}
