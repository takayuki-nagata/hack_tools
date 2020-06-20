#ifndef _PARSER_H
#define _PARSER_H

#include <stdbool.h>

enum {
	A_COMMAND,
	C_COMMAND,
	L_COMMAND,
};

extern void parser_open(const char *fpath);
extern void parser_close(void);
extern bool parser_has_more_commands(void);
extern void parser_advanced(void);
extern int parser_command_type(void);
extern char* parser_symbol(void);
extern char* parser_dest(void);
extern char* parser_comp(void);
extern char* parser_jump(void);

#endif /* _PARSER_H */
