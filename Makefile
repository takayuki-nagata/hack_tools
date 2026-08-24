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

test-all: test m2h-test

# Python / m2h targets
m2h-sync:
	@cd m2h && uv sync

m2h-test:
	@echo "=== Running m2h pytest ==="
	@cd m2h && uv run pytest

m2h-coverage:
	@echo "=== Running m2h pytest with coverage ==="
	@cd m2h && uv run pytest --cov=m2h --cov-report=term-missing

m2h-typecheck:
	@echo "=== Running m2h mypy typecheck ==="
	@cd m2h && uv run mypy src/ tests/

m2h-lint:
	@echo "=== Running m2h ruff lint ==="
	@cd m2h && uv run ruff check src/ tests/

m2h-format:
	@echo "=== Formatting m2h with ruff ==="
	@cd m2h && uv run ruff format src/ tests/

m2h-format-check:
	@echo "=== Checking m2h formatting with ruff ==="
	@cd m2h && uv run ruff format --check src/ tests/

m2h-mutation:
	@echo "=== Running m2h mutation testing (mutmut) ==="
	@cd m2h && uv run mutmut run || true
	@cd m2h && uv run mutmut results

MSP430_GCC_URL ?= https://dr-download.ti.com/software-development/ide-configuration-compiler-or-debugger/MD-LlCjWuAbzH/9.3.1.2/msp430-gcc-9.3.1.11_linux64.tar.bz2
LOCAL_TOOLCHAIN_DIR ?= $(HOME)/.local/msp430-gcc
LOCAL_BIN_DIR ?= $(HOME)/.local/bin

install-msp430-gcc:
	@echo "=== Downloading and installing MSP430 GCC 9.3.1.11 to $(LOCAL_TOOLCHAIN_DIR) ==="
	@mkdir -p $(LOCAL_TOOLCHAIN_DIR) $(LOCAL_BIN_DIR)
	@curl -fsSL $(MSP430_GCC_URL) | tar -xjf - -C $(LOCAL_TOOLCHAIN_DIR) --strip-components=1
	@ln -sf $(LOCAL_TOOLCHAIN_DIR)/bin/msp430-elf-gcc $(LOCAL_BIN_DIR)/msp430-elf-gcc
	@ln -sf $(LOCAL_TOOLCHAIN_DIR)/bin/msp430-elf-gcc $(LOCAL_BIN_DIR)/msp430-gcc
	@echo "MSP430 GCC installed successfully. Ensure $(LOCAL_BIN_DIR) is in your PATH."

# End-to-End Test for C compilation pipeline (requires gcc-msp430 or msp430-elf-gcc)
e2e-test: all
	@echo "=== Running End-to-End C Compilation Tests ==="
	@mkdir -p test_out
	@which msp430-gcc >/dev/null 2>&1 || which msp430-elf-gcc >/dev/null 2>&1 || [ -x $(LOCAL_BIN_DIR)/msp430-gcc ] || [ -x $(LOCAL_BIN_DIR)/msp430-elf-gcc ] || (echo "MSP430 GCC not found, skipping E2E C tests." && exit 0); \
	for c_file in tests/c/*.c; do \
		base=$$(basename "$$c_file" .c); \
		echo "Compiling and assembling $$c_file -> test_out/$$base.hack ..."; \
		cd m2h && uv run hcc ../$$c_file -o ../test_out/$$base.hack && cd ..; \
		test -s test_out/$$base.hack || exit 1; \
		echo "PASSED: test_out/$$base.hack generated successfully."; \
	done

coverage: clean
	@$(MAKE) all COVERAGE=1
	@HAS_BIN="$(CURDIR)/has/has" bash tests/run_tests.sh
	@echo ""
	@echo "=== Coverage Summary (has: gcov) ==="
	@cd has && gcov -b -c *.c
	@echo ""

coverage-all: coverage m2h-coverage

sanitize: clean
	@$(MAKE) all SANITIZE=1
	@HAS_BIN="$(CURDIR)/has/has" bash tests/run_tests.sh

format:
	@find has tests -name "*.c" -o -name "*.h" | xargs clang-format -i
	@echo "C formatting complete."

format-check:
	@find has tests -name "*.c" -o -name "*.h" | xargs clang-format --dry-run --Werror
	@echo "C format check passed."

format-all: format m2h-format

format-check-all: format-check m2h-format-check

lint:
	@$(MAKE) clean
	@$(MAKE) all CFLAGS="$(CFLAGS) -Werror"

lint-all: lint m2h-lint m2h-typecheck

install: has
	install -d $(DESTDIR)$(BINDIR)
	install -m 755 has/has $(DESTDIR)$(BINDIR)/has

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/has

clean:
	$(MAKE) -C has clean
	rm -rf test_out tests/out *.gcno *.gcda *.gcov has/*.gcno has/*.gcda has/*.gcov tests/*.o tests/*.gcno tests/*.gcda tests/unit_test m2h/.coverage m2h/.pytest_cache m2h/.mypy_cache m2h/htmlcov

.PHONY: all has test test-all coverage coverage-all sanitize format format-check format-all format-check-all lint lint-all install uninstall clean \
        m2h-sync m2h-test m2h-coverage m2h-typecheck m2h-lint m2h-format m2h-format-check m2h-mutation e2e-test install-msp430-gcc
