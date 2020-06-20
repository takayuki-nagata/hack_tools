#ifndef _CODE_H
#define _CODE_H

#include <stdint.h>

#define CODE_ERROR ((uint8_t)0xff)

#define CODE_COMPOSE(dest,comp,jump) \
       ((0x7<<13)|((comp)<<6)|((dest)<<3)|(jump))

extern uint8_t code_dest(const char *mnemonic);
extern uint8_t code_comp(const char *mnemonic);
extern uint8_t code_jump(const char *mnemonic);

#endif /* _CODE_H */
