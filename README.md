# hack_tools

[![CI](https://github.com/takayuki-nagata/hack_tools/actions/workflows/ci.yml/badge.svg)](https://github.com/takayuki-nagata/hack_tools/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Language: C99](https://img.shields.io/badge/Language-C99-orange.svg)](https://en.wikipedia.org/wiki/C99)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![uv: Managed](https://img.shields.io/badge/Package_Manager-uv-purple.svg)](https://docs.astral.sh/uv/)

A lightweight, robust toolchain for the **Hack CPU** architecture (from the *Nand2Tetris* / *The Elements of Computing Systems* project), originally built for [takayuki-nagata/hack_cpu](https://github.com/takayuki-nagata/hack_cpu).

---

## Tools

### 1. `has` (Hack Assembler)
An optimizing 2-pass Hack Assembler written in standard C99.
- Translates Hack assembly source files (`.asm`) into binary machine instructions.
- Supports multiple output formats:
  - **Hack binary text** (`.hack`): standard 16-character `'0'`/`'1'` ASCII strings per instruction.
  - **Raw binary** (`.bin`): 16-bit big-endian binary image.
  - **Xilinx COE** (`.coe`): Memory initialization file format for FPGA synthesis and ROM generation.
- Supports predefined symbols (`SP`, `LCL`, `ARG`, `THIS`, `THAT`, `R0`..`R15`, `SCREEN`, `KBD`), forward/backward labels (`(LABEL)`), and variable allocation (`RAM[16..]`).

### 2. `hcc` (Hack C Compiler Frontend)
An integrated compiler frontend that compiles C99 code directly into Hack machine code (`.hack`, `.bin`, `.coe`) with a single command.
- Orchestrates `msp430-gcc` $\to$ `m2h` $\to$ `has` in a seamless pipeline.
- Automatically selects optimal compilation flags (`-O2 -ffreestanding -fno-exceptions -nostdlib -mhwmult=none`).

### 3. `m2h` (MSP430 to Hack Transpiler)
A zero-runtime-dependency transpiler written in Python (managed with `uv`) that maps GCC-generated 16-bit MSP430 assembly (`.s`) into Hack assembly (`.asm`).
- For detailed ABI, memory maps, and instruction mappings, see [**`m2h/docs/SPECIFICATION.md`**](m2h/docs/SPECIFICATION.md).

---

## Pipeline

```text
[ C Source: file.c ]
        │
        ▼ (msp430-gcc -S -O2 -ffreestanding ...)
[ MSP430 Asm: file.s ]
        │
        ▼ (m2h)
[ Hack Asm: file.asm ]
        │
        ▼ (has)
[ Hack Binary: .hack / .bin / .coe ]
```

---

## Building and Installation

### Requirements
- C99 C compiler (`gcc` or `clang`)
- Python 3.9+ and [`uv`](https://docs.astral.sh/uv/)
- MSP430 GCC (`gcc-msp430` / `msp430-gcc`, optional for C compilation)

### Build
```bash
make
```

### Install `has`
```bash
sudo make install PREFIX=/usr/local
```

---

## Usage

### 1. Compile C Code with `hcc`

```bash
# Compile main.c directly to main.hack
cd m2h && uv run hcc ../tests/c/sum.c -o sum.hack

# Output as raw binary (.bin) or Xilinx COE (.coe)
cd m2h && uv run hcc -r -o sum.bin ../tests/c/sum.c
cd m2h && uv run hcc -c -o sum.coe ../tests/c/sum.c

# Stop after generating Hack assembly (.asm)
cd m2h && uv run hcc -S ../tests/c/sum.c -o sum.asm
```

### 2. Assemble Hack Assembly with `has`

```bash
# Assemble Prog.asm -> Prog.hack
has Prog.asm

# Output raw binary (.bin) or Xilinx COE (.coe)
has -r -o rom.bin Prog.asm
has -c -o rom.coe Prog.asm
```

### 3. Transpile MSP430 Assembly with `m2h`

```bash
cd m2h && uv run m2h input.s -o output.asm
```

---

## Testing & Quality Assurance

### Run All Tests
```bash
make test
```

### Code Coverage (100% Target)
```bash
# Measures C coverage (gcov) and Python coverage (pytest-cov)
make coverage
```

### Type Checking & Linting
```bash
# Run mypy strict type check, ruff lint, and clang-format check
make lint
make format-check
```

### Mutation Testing (`mutmut`)
```bash
make m2h-mutation
```

### End-to-End C Compilation Tests
```bash
make e2e-test
```

---

## Related Projects

- [takayuki-nagata/hack_cpu](https://github.com/takayuki-nagata/hack_cpu): Hardware implementation of the Hack CPU in Verilog/HDL.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

SPDX-License-Identifier: MIT  
Copyright (c) 2020-2026 Takayuki Nagata
