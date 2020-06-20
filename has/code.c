#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include "code.h"

#define CA 0x40
#define C1 0x20
#define C2 0x10
#define C3 0x8
#define C4 0x4
#define C5 0x2
#define C6 0x1

#define D1 0x4
#define D2 0x2
#define D3 0x1

#define J1 0x4
#define J2 0x2
#define J3 0x1

typedef struct
{
	char *mnemonic;
	uint8_t binary;
} instruction_table_t;

const instruction_table_t comp_tbl0[] = {
	{ "0"  , C1|00|C3|00|C5|00 },
	{ "1"  , C1|C2|C3|C4|C5|C6 },
	{ "-1" , C1|C2|C3|00|C5|00 },
	{ "D"  , 00|00|C3|C4|00|00 },
	{ "A"  , C1|C2|00|00|00|00 },
	{ "!D" , 00|00|C3|C4|00|C6 },
	{ "!A" , C1|C2|00|00|00|C6 },
	{ "-D" , 00|00|C3|C4|C5|C6 },
	{ "-A" , C1|C2|00|00|C5|C6 },
	{ "D+1", 00|C2|C3|C4|C5|C6 },
	{ "A+1", C1|C2|00|C4|C5|C6 },
	{ "D-1", 00|00|C3|C4|C5|00 },
	{ "A-1", C1|C2|00|00|C5|00 },
	{ "D+A", 00|00|00|00|C5|00 },
	{ "D-A", 00|C2|00|00|C5|C6 },
	{ "A-D", 00|00|00|C4|C5|C6 },
	{ "D&A", 00|00|00|00|00|00 },
	{ "D|A", 00|C2|00|C4|00|C6 },
	{ "", 0},
};

const instruction_table_t comp_tbl1[] = {
	{ "M"  , C1|C2|00|00|00|00 },
	{ "!M" , C1|C2|00|00|00|C6 },
	{ "-M" , C1|C2|00|00|C5|C6 },
	{ "M+1", C1|C2|00|C4|C5|C6 },
	{ "M-1", C1|C2|00|00|C5|00 },
	{ "D+M", 00|00|00|00|C5|00 },
	{ "D-M", 00|C2|00|00|C5|C6 },
	{ "M-D", 00|00|00|C4|C5|C6 },
	{ "D&M", 00|00|00|00|00|00 },
	{ "D|M", 00|C2|00|C4|00|C6 },
	{ "", 0},
};

const instruction_table_t dest_tbl[] = {
	{ "M"  , 00|00|D3 },
	{ "D"  , 00|D2|00 },
	{ "MD" , 00|D2|D3 },
	{ "A"  , D1|00|00 },
	{ "AM" , D1|00|D3 },
	{ "AD" , D1|D2|00 },
	{ "AMD", D1|D2|D3 },
	{ "", 0},
};

const instruction_table_t jump_tbl[] = {
	{ "JGT", 00|00|J3 },
	{ "JEG", 00|J2|00 },
	{ "JGE", 00|J2|J3 },
	{ "JLT", J1|00|00 },
	{ "JNE", J1|00|J3 },
	{ "JLE", J1|J2|00 },
	{ "JMP", J1|J2|J3 },
	{ "", 0},
};

static void code_error(const char *mnemonic, const char *msg)
{
	printf("code error: %s: %s\n", mnemonic, msg);
}

static uint8_t search_tbl(const instruction_table_t *tbl, const char *mnemonic)
{
	int i = 0;
	while (strlen(tbl[i].mnemonic)) {
		if (!strcmp(mnemonic, tbl[i].mnemonic)) {
			return tbl[i].binary;
		}
		i++;
	}
	return CODE_ERROR;
}

uint8_t code_dest(const char *mnemonic)
{
	uint8_t binary;

	if (mnemonic) {
		if (CODE_ERROR == (binary = search_tbl(dest_tbl, mnemonic)))
			code_error(mnemonic, "invalid dest mnemonic");
		return binary;
	}
	return 0x00;
}

uint8_t code_comp(const char *mnemonic)
{
	uint8_t binary;

	if (!mnemonic) {
		code_error(NULL, "illegal mnemonic");
		return 0xff;
	}

	if (CODE_ERROR == (binary = search_tbl(comp_tbl1, mnemonic))) {
		if (CODE_ERROR == (binary = search_tbl(comp_tbl0, mnemonic)))
			code_error(mnemonic, "invalid comp mnemonic");
		return binary;
	}
	return binary|CA;
}

uint8_t code_jump(const char *mnemonic)
{
	uint8_t binary;
	if (mnemonic) {
		if (CODE_ERROR == (binary = search_tbl(jump_tbl, mnemonic)))
			code_error(mnemonic, "invalid jump mnemonic");
		return binary;
	}
	return 0x00;
}
