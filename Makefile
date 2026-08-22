# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

CC ?= gcc
PREFIX ?= /usr/local
BINDIR ?= $(PREFIX)/bin

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

UNIT_TEST = tests/unit_test
UNIT_OBJS = has/assembler.o has/parser.o has/code.o has/symbol_table.o has/output_formatter.o tests/unit_test.o

export CC CFLAGS LDFLAGS PREFIX BINDIR

all: has $(UNIT_TEST)

has:
	$(MAKE) -C has

$(UNIT_TEST): has tests/unit_test.o
	$(CC) $(UNIT_OBJS) $(LDFLAGS) -o $@

tests/unit_test.o: tests/unit_test.c
	$(CC) $(CFLAGS) -c $< -o $@

test: all
	@bash tests/run_tests.sh

coverage: clean
	@$(MAKE) all COVERAGE=1
	@HAS_BIN="$(CURDIR)/has/has" bash tests/run_tests.sh
	@echo ""
	@echo "=== Coverage Summary (gcov) ==="
	@cd has && gcov -b -c *.c
	@echo ""
	@echo "Coverage files generated in has/"

sanitize: clean
	@$(MAKE) all SANITIZE=1
	@HAS_BIN="$(CURDIR)/has/has" bash tests/run_tests.sh

format:
	@find has tests -name "*.c" -o -name "*.h" | xargs clang-format -i
	@echo "Formatting complete."

format-check:
	@find has tests -name "*.c" -o -name "*.h" | xargs clang-format --dry-run --Werror
	@echo "Format check passed."

lint:
	@$(MAKE) clean
	@$(MAKE) all CFLAGS="$(CFLAGS) -Werror"

install: has
	install -d $(DESTDIR)$(BINDIR)
	install -m 755 has/has $(DESTDIR)$(BINDIR)/has

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/has

clean:
	$(MAKE) -C has clean
	rm -rf test_out tests/out *.gcno *.gcda *.gcov has/*.gcno has/*.gcda has/*.gcov tests/*.o tests/*.gcno tests/*.gcda tests/unit_test

.PHONY: all has test coverage sanitize format format-check lint install uninstall clean
