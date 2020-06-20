#ifndef _SYMBOL_TABLE_H
#define _SYMBOL_TABLE_H

#include <stdint.h>

#define SYMTBL_ERROR ((uint16_t)0xffff)

extern void symbol_table_open(void);
extern void symbol_table_close(void);
extern void symbol_table_add_entry(const char *symbol, const uint16_t address);
extern bool symbol_table_contains(const char *symbol);
extern uint16_t symbol_table_get_address(const char *symbol);

#endif /* _SYMBOL_TABLE_H */
