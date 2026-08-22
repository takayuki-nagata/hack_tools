# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

CC ?= gcc
CFLAGS ?= -std=c99 -Wall -Wextra -Wpedantic -Wshadow -Wconversion -Wstrict-prototypes -O2
LDFLAGS ?=

ifeq ($(DEBUG), 1)
	CFLAGS += -g -O0
endif

ifeq ($(SANITIZE), 1)
	CFLAGS += -fsanitize=address,undefined -g
	LDFLAGS += -fsanitize=address,undefined
endif

ifeq ($(COVERAGE), 1)
	CFLAGS += --coverage -O0 -g
	LDFLAGS += --coverage
endif

SRCS = main.c assembler.c parser.c code.c symbol_table.c output_formatter.c
OBJS = $(SRCS:.c=.o)
TARGET = has

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(OBJS) $(LDFLAGS) -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET) *.gcno *.gcda *.gcov

.PHONY: all clean
