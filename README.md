# hack_tools

[![CI](https://github.com/takayuki-nagata/hack_tools/actions/workflows/ci.yml/badge.svg)](https://github.com/takayuki-nagata/hack_tools/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Language: C99](https://img.shields.io/badge/Language-C99-orange.svg)](https://en.wikipedia.org/wiki/C99)

A lightweight, robust toolchain for the **Hack CPU** architecture (from the *Nand2Tetris* / *The Elements of Computing Systems* project), originally built for [takayuki-nagata/hack_cpu](https://github.com/takayuki-nagata/hack_cpu).

---

## Tools

- **`has`**: An optimizing 2-pass Hack Assembler written in standard C99.
  - Translates Hack assembly source files (`.asm`) into binary machine instructions.
  - Supports multiple output formats:
    - **Hack binary text** (`.hack`): standard 16-character `'0'`/`'1'` ASCII strings per instruction.
    - **Raw binary** (`.bin`): 16-bit big-endian binary image.
    - **Xilinx COE** (`.coe`): Memory initialization file format for FPGA synthesis and ROM generation.
  - Supports predefined symbols (`SP`, `LCL`, `ARG`, `THIS`, `THAT`, `R0`..`R15`, `SCREEN`, `KBD`), forward/backward labels (`(LABEL)`), and user-defined variable allocation (`RAM[16..]`).

---

## Building and Installation

### Requirements
- C99-compliant C compiler (`gcc` or `clang`)
- GNU Make (`make`)
- Standard POSIX shell / coreutils (for testing)

### Build
To build the assembler:
```bash
make
```
The compiled binary will be placed in `has/has`.

### Install / Uninstall
To install `has` to `/usr/local/bin` (or custom `PREFIX`):
```bash
sudo make install
```
To customize the install directory:
```bash
make install PREFIX=$HOME/.local
```
To uninstall:
```bash
sudo make uninstall
```

---

## Usage

```text
Usage: has [OPTION]... FILE
Assemble Hack assembly (.asm) into machine code.

Options:
  -o, --outfile=FILE       Output to FILE.
  -r, --raw                Use raw binary format (.bin).
  -c, --coe                Use Xilinx COE format (.coe).
  -s, --stdout             Output to stdout instead of a file.
  -h, --help               Display this help text and exit.
  -v, --version            Output version information and exit.

Default output format is Hack text binary (.hack).
```

### Examples

1. **Assemble `.asm` to `.hack`** (default output file `Prog.hack` in the same directory):
   ```bash
   has Prog.asm
   ```

2. **Specify output file name**:
   ```bash
   has -o output.hack Prog.asm
   ```

3. **Output raw binary (`.bin`) for emulator/ROM loading**:
   ```bash
   has -r -o rom.bin Prog.asm
   ```

4. **Output Xilinx COE (`.coe`) for FPGA block RAM**:
   ```bash
   has -c -o rom.coe Prog.asm
   ```

5. **Print assembled output directly to stdout**:
   ```bash
   has -s Prog.asm
   ```

---

## Testing & Quality Assurance

This repository includes a completely self-contained, comprehensive test suite covering all instruction variants, symbol resolution edge cases, format outputs, and error handling.

### Run Automated Tests
```bash
make test
```

### Code Coverage
Measure line and branch coverage using `gcov`:
```bash
make coverage
```

### Address & Undefined Behavior Sanitizers
```bash
make sanitize
```

### Lint & Format Check
```bash
make lint
make format-check
```

---

## Related Projects

- [takayuki-nagata/hack_cpu](https://github.com/takayuki-nagata/hack_cpu): Hardware implementation of the Hack CPU in Verilog/HDL.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

SPDX-License-Identifier: MIT  
Copyright (c) 2020-2026 Takayuki Nagata
