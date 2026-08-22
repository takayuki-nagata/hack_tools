# m2h & hcc: MSP430 to Hack Transpiler & Hack C Compiler

`m2h` is an MSP430 assembly to Hack assembly transpiler, and `hcc` is the integrated C compiler frontend for the **Hack CPU** architecture (from *Nand2Tetris* / [takayuki-nagata/hack_cpu](https://github.com/takayuki-nagata/hack_cpu)).

---

## Features

- **Direct C Compilation (`hcc`)**: Compile standard C99 code directly into Hack machine code (`.hack`, `.bin`, `.coe`) with a single command.
- **Assembly Transpilation (`m2h`)**: Transpile GCC-generated MSP430 assembly (`.s`) into clean Hack assembly (`.asm`).
- **Zero Runtime Dependencies**: Written in standard Python 3.9+, using only the Python standard library.
- **Specification Documentation**: Detailed architectural and ABI specification available at [`docs/SPECIFICATION.md`](docs/SPECIFICATION.md).

---

## Quick Start

### 1. Compile C code directly with `hcc`
```bash
# Compiles main.c -> main.hack
uv run hcc main.c

# Output as raw binary (.bin) or Xilinx COE (.coe)
uv run hcc -r -o main.bin main.c
uv run hcc -c -o main.coe main.c
```

### 2. Transpile MSP430 assembly with `m2h`
```bash
# Transpile foo.s to foo.asm
uv run m2h foo.s -o foo.asm

# Assemble with has
has foo.asm
```

---

## Development & Testing

Managed with [`uv`](https://docs.astral.sh/uv/):

```bash
# Run unit tests and check 100% coverage
uv run pytest --cov=m2h --cov-report=term-missing

# Strict type checking with mypy
uv run mypy src/ tests/

# Lint and format check with ruff
uv run ruff check src/ tests/
uv run ruff format --check src/ tests/

# Mutation testing with mutmut
uv run mutmut run
```
