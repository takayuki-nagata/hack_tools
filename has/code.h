// SPDX-License-Identifier: MIT
/*
 * Copyright (c) 2020-2026 Takayuki Nagata
 */

#ifndef HAS_CODE_H
#define HAS_CODE_H

#include <stdint.h>

#define CODE_ERROR ((uint8_t)0xff)

#define CODE_COMPOSE(dest, comp, jump)                                                             \
    ((uint16_t)(((uint16_t)0x7 << 13) | (((uint16_t)(comp) & 0x7f) << 6) |                         \
                (((uint16_t)(dest) & 0x7) << 3) | ((uint16_t)(jump) & 0x7)))

uint8_t code_dest(const char *mnemonic);
uint8_t code_comp(const char *mnemonic);
uint8_t code_jump(const char *mnemonic);

#endif /* HAS_CODE_H */
