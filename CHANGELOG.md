# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-08-22

### Added
- **`has` (Hack Assembler in C99)**:
  - Supports three output formats: Hack ASCII (`.hack`), raw binary (`.bin`), and Xilinx memory initialization COE (`.coe`).
  - Implements complete two-pass symbol resolution for predefined symbols (`R0`-`R15`, `SP`, `LCL`, `ARG`, `THIS`, `THAT`, `SCREEN`, `KBD`), user labels (`(LABEL)`), and variables (`@var`).
  - Comprehensive test suite with 94%+ line coverage (`gcov`), verified with AddressSanitizer (ASan), UndefinedBehaviorSanitizer (UBSan), and Valgrind (zero memory leaks).
- **`m2h` (MSP430 to Hack Transpiler in Python)**:
  - Zero runtime dependencies (standard library only), managed with `uv`.
  - Robust parser supporting comments (including C-style block comments `/* ... */`), directives, and all 6 MSP430 addressing modes (Register, Immediate with negative/expression support, Indirect, Autoincrement, Indexed, Absolute).
  - Code emitter mapping arithmetic/logic (`mov`, `add`, `sub`, `and`, `bis`, `bic`, `xor`, `clr`, `inv`, `neg`), shifts (`rla`, `rlc`), bit test (`bit`), conditional jumps (`jeq`, `jne`, `jge`, `jl`, `jmp`, `br`), and call/return (`push`, `pop`, `call`, `ret`).
  - Standard runtime startup (`crt0.py`) initializing stack pointer (`RAM[256]`) and halting on completion.
  - 100.00% Pytest test coverage (`pytest-cov`), strict type safety (`mypy --strict`), and strict linting (`ruff`).
- **`hcc` (Hack C Compiler Frontend)**:
  - One-command compiler pipeline compiling standard C99 source files directly to `.hack`, `.bin`, or `.coe` formats.
  - Automatic freestanding compilation flags orchestration (`-std=c99 -O2 -ffreestanding -fno-exceptions -nostdlib`).
- **Documentation & CI/CD**:
  - Detailed architectural, memory layout, ABI, and instruction mapping specification ([`m2h/docs/SPECIFICATION.md`](m2h/docs/SPECIFICATION.md)).
  - Comprehensive continuous integration (`.github/workflows/ci.yml`) covering Linux/macOS build matrices, C sanitizers, Valgrind, coverage, and end-to-end C compilation.
  - Continuous delivery workflow (`.github/workflows/cd.yml`) for automated multi-platform binary packaging and GitHub Releases.
