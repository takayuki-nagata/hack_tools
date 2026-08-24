# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-08-24

### Added
- **`libm2h` Built-in Software Runtime Helper Library** (`m2h/src/m2h/runtime.py`):
  - 16-bit integer multiplication (`__mspabi_mpyi`, `__mulhi3`) using software shift-and-add.
  - 16-bit signed/unsigned integer division and modulo (`__m2h_udivmod`, `__mspabi_divi`, `__divhi3`, `__mspabi_divu`, `__udivhi3`, `__mspabi_remi`, `__modhi3`, `__mspabi_remu`, `__umodhi3`).
  - Function epilogue callee-saved register restoration helpers (`__mspabi_func_epilog_1` through `__mspabi_func_epilog_7`) to support GCC `-O2` space optimization.
  - 1-bit right shift helpers (`__m2h_rrc` for logical shift, `__m2h_rra` for arithmetic shift) and dynamic left shift (`__mspabi_slli`, `__ashlhi3`).
- **16 Real-World End-to-End C Benchmark Suite** (`tests/c/`):
  - Cooperative Mini-RTOS task scheduler (`rtos_scheduler.c`) with TCBs and function pointer dispatch.
  - Data structures: Singly-linked list reversal (`struct_list.c`), Binary Search Tree (`recursion_tree.c`), Circular FIFO ring buffer (`ring_buffer.c`).
  - Algorithms: In-place recursive QuickSort and binary search (`quicksort.c`), 2D matrix multiplication and 3x3 determinant (`matrix_ops.c`).
  - String parsing: `my_atoi`, `my_itoa`, and tokenized arithmetic expression evaluator (`string_parser.c`).
  - Bit manipulation & arithmetic boundary edge cases: Popcount, byte swap, power of two, sign extension, negative division/modulo (`bit_twiddling.c`, `math.c`).
  - Control flow: Short-circuit evaluations (`&&`, `||`), nested loop `break`/`continue`/`goto`, and finite state machine (`control_flow.c`, `switch_dispatch.c`).
  - Memory-mapped hardware I/O: Screen graphics and pixel bitmap manipulation (`screen_graphics.c`).
- **Instruction Support in `m2h`**:
  - Unsigned conditional jump instructions (`jlo`, `jhs`, `jc`, `jnc`).
  - Indirect function call via registers (`call Rn`).
  - Status flag manipulation and NOP instructions (`clrc`, `setc`, `clrn`, `setn`, `clrz`, `setz`, `dint`, `eint`, `nop`).
- **Compiler Toolchain Integration**:
  - `make install-msp430-gcc` target to download and install official TI MSP430 GCC 9.3.1.11 to `~/.local/msp430-gcc`.
  - Automatic toolchain detection and version verification in `hcc` with warnings for outdated compilers.
  - Automatic injection of optimal compilation flags (`-mmax-inline-shift=64`, `-fno-jump-tables`).

### Changed
- **Unified Downward Stack Growth**:
  - Converted `push`, `pop`, `call`, `ret`, `crt0`, and epilogue helpers to downward stack growth (`RAM[16384]` downward) to match MSP430 GCC native frame layout (`0(SP)`).
- **CI/CD Modernization**:
  - Upgraded CI runners to `ubuntu-latest` with cached TI MSP430 GCC toolchain.

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
