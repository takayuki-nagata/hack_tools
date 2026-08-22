# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

"""Command-line interface for hcc (Hack C Compiler frontend)."""

import argparse
import sys
from typing import Optional

from m2h import __version__
from m2h.driver import CompilerDriver


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_parser__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_parser__mutmut)
def build_parser() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_orig() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_1() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = None
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_2() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog=None,
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_3() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description=None,
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_4() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_5() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_6() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="XXhccXX",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_7() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="HCC",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_8() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="XXCompile C code directly into Hack machine code.XX",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_9() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="compile c code directly into hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_10() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="COMPILE C CODE DIRECTLY INTO HACK MACHINE CODE.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_11() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument(None, metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_12() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar=None, help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_13() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help=None)
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_14() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument(metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_15() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_16() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", )
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_17() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("XXinput_fileXX", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_18() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("INPUT_FILE", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_19() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="XXFILE.cXX", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_20() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="file.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_21() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.C", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_22() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="XXC source code input fileXX")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_23() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="c source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_24() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C SOURCE CODE INPUT FILE")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_25() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument(None, "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_26() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", None, metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_27() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar=None, help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_28() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help=None)
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_29() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_30() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_31() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_32() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", )
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_33() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("XX-oXX", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_34() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-O", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_35() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "XX--outfileXX", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_36() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--OUTFILE", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_37() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="XXFILEXX", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_38() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="file", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_39() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="XXOutput fileXX")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_40() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_41() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="OUTPUT FILE")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_42() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument(None, "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_43() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", None, action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_44() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action=None, help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_45() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help=None)
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_46() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_47() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_48() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_49() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", )
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_50() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("XX-rXX", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_51() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-R", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_52() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "XX--rawXX", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_53() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--RAW", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_54() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="XXstore_trueXX", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_55() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="STORE_TRUE", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_56() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="XXOutput raw binary format (.bin)XX")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_57() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_58() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="OUTPUT RAW BINARY FORMAT (.BIN)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_59() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument(None, "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_60() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", None, action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_61() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action=None, help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_62() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help=None)
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_63() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_64() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_65() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_66() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", )
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_67() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("XX-cXX", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_68() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-C", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_69() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "XX--coeXX", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_70() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--COE", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_71() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="XXstore_trueXX", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_72() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="STORE_TRUE", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_73() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="XXOutput Xilinx COE format (.coe)XX")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_74() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="output xilinx coe format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_75() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="OUTPUT XILINX COE FORMAT (.COE)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_76() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        None, "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_77() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", None, action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_78() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action=None, help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_79() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help=None
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_80() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_81() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_82() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_83() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_84() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "XX-sXX", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_85() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-S", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_86() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "XX--stdoutXX", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_87() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--STDOUT", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_88() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="XXstore_trueXX", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_89() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="STORE_TRUE", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_90() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="XXOutput to stdout instead of a fileXX"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_91() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_92() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="OUTPUT TO STDOUT INSTEAD OF A FILE"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_93() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        None,
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_94() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        None,
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_95() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action=None,
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_96() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help=None,
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_97() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_98() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_99() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_100() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_101() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "XX-SXX",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_102() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-s",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_103() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "XX--assemble-onlyXX",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_104() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--ASSEMBLE-ONLY",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_105() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="XXstore_trueXX",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_106() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="STORE_TRUE",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_107() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="XXCompile and transpile to Hack assembly (.asm) onlyXX",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_108() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="compile and transpile to hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_109() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="COMPILE AND TRANSPILE TO HACK ASSEMBLY (.ASM) ONLY",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_110() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        None, "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_111() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", None, action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_112() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action=None, help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_113() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help=None
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_114() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_115() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_116() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_117() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_118() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "XX-kXX", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_119() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-K", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_120() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "XX--keepXX", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_121() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--KEEP", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_122() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="XXstore_trueXX", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_123() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="STORE_TRUE", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_124() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="XXKeep intermediate .s and .asm filesXX"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_125() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_126() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="KEEP INTERMEDIATE .S AND .ASM FILES"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_127() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        None,
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_128() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        None,
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_129() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default=None,
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_130() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help=None,
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_131() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_132() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_133() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_134() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_135() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "XX-OXX",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_136() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-o",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_137() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "XX--opt-levelXX",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_138() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--OPT-LEVEL",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_139() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="XX-O2XX",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_140() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-o2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_141() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="XXOptimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)XX",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_142() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="optimization level (e.g. -o2, -o3, -os, -o0, default: -o2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_143() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="OPTIMIZATION LEVEL (E.G. -O2, -O3, -OS, -O0, DEFAULT: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_144() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        None, metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_145() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar=None, help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_146() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help=None
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_147() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_148() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_149() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_150() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "XX--ccXX", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_151() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--CC", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_152() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="XXCOMPILERXX", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_153() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="compiler", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_154() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="XXCustom MSP430 C compiler path (default: msp430-gcc)XX"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_155() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="custom msp430 c compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_156() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="CUSTOM MSP430 C COMPILER PATH (DEFAULT: MSP430-GCC)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_157() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        None, metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_158() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar=None, help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_159() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help=None
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_160() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_161() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_162() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_163() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "XX--hasXX", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_164() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--HAS", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_165() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="XXASSEMBLERXX", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_166() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="assembler", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_167() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="XXCustom has assembler path (default: has)XX"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_168() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_169() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="CUSTOM HAS ASSEMBLER PATH (DEFAULT: HAS)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_170() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        None, action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_171() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action=None, help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_172() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help=None
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_173() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_174() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_175() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_176() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "XX--no-crt0XX", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_177() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--NO-CRT0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_178() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="XXstore_trueXX", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_179() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="STORE_TRUE", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_180() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="XXDo not include startup runtime (crt0)XX"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_181() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_182() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="DO NOT INCLUDE STARTUP RUNTIME (CRT0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_183() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument(None, "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_184() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", None, action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_185() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action=None, version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_186() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=None)
    return parser


def x_build_parser__mutmut_187() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_188() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_189() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_190() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", )
    return parser


def x_build_parser__mutmut_191() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("XX-vXX", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_192() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_193() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "XX--versionXX", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_194() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--VERSION", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_195() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="XXversionXX", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_196() -> argparse.ArgumentParser:
    """Build argument parser for hcc."""
    parser = argparse.ArgumentParser(
        prog="hcc",
        description="Compile C code directly into Hack machine code.",
    )
    parser.add_argument("input_file", metavar="FILE.c", help="C source code input file")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output file")
    parser.add_argument("-r", "--raw", action="store_true", help="Output raw binary format (.bin)")
    parser.add_argument("-c", "--coe", action="store_true", help="Output Xilinx COE format (.coe)")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "-S",
        "--assemble-only",
        action="store_true",
        help="Compile and transpile to Hack assembly (.asm) only",
    )
    parser.add_argument(
        "-k", "--keep", action="store_true", help="Keep intermediate .s and .asm files"
    )
    parser.add_argument(
        "-O",
        "--opt-level",
        default="-O2",
        help="Optimization level (e.g. -O2, -O3, -Os, -O0, default: -O2)",
    )
    parser.add_argument(
        "--cc", metavar="COMPILER", help="Custom MSP430 C compiler path (default: msp430-gcc)"
    )
    parser.add_argument(
        "--has", metavar="ASSEMBLER", help="Custom has assembler path (default: has)"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="VERSION", version=f"%(prog)s {__version__}")
    return parser

mutants_x_build_parser__mutmut['_mutmut_orig'] = x_build_parser__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_1'] = x_build_parser__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_2'] = x_build_parser__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_3'] = x_build_parser__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_4'] = x_build_parser__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_5'] = x_build_parser__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_6'] = x_build_parser__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_7'] = x_build_parser__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_8'] = x_build_parser__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_9'] = x_build_parser__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_10'] = x_build_parser__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_11'] = x_build_parser__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_12'] = x_build_parser__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_13'] = x_build_parser__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_14'] = x_build_parser__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_15'] = x_build_parser__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_16'] = x_build_parser__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_17'] = x_build_parser__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_18'] = x_build_parser__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_19'] = x_build_parser__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_20'] = x_build_parser__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_21'] = x_build_parser__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_22'] = x_build_parser__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_23'] = x_build_parser__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_24'] = x_build_parser__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_25'] = x_build_parser__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_26'] = x_build_parser__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_27'] = x_build_parser__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_28'] = x_build_parser__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_29'] = x_build_parser__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_30'] = x_build_parser__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_31'] = x_build_parser__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_32'] = x_build_parser__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_33'] = x_build_parser__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_34'] = x_build_parser__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_35'] = x_build_parser__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_36'] = x_build_parser__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_37'] = x_build_parser__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_38'] = x_build_parser__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_39'] = x_build_parser__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_40'] = x_build_parser__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_41'] = x_build_parser__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_42'] = x_build_parser__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_43'] = x_build_parser__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_44'] = x_build_parser__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_45'] = x_build_parser__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_46'] = x_build_parser__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_47'] = x_build_parser__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_48'] = x_build_parser__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_49'] = x_build_parser__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_50'] = x_build_parser__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_51'] = x_build_parser__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_52'] = x_build_parser__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_53'] = x_build_parser__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_54'] = x_build_parser__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_55'] = x_build_parser__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_56'] = x_build_parser__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_57'] = x_build_parser__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_58'] = x_build_parser__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_59'] = x_build_parser__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_60'] = x_build_parser__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_61'] = x_build_parser__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_62'] = x_build_parser__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_63'] = x_build_parser__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_64'] = x_build_parser__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_65'] = x_build_parser__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_66'] = x_build_parser__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_67'] = x_build_parser__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_68'] = x_build_parser__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_69'] = x_build_parser__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_70'] = x_build_parser__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_71'] = x_build_parser__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_72'] = x_build_parser__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_73'] = x_build_parser__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_74'] = x_build_parser__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_75'] = x_build_parser__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_76'] = x_build_parser__mutmut_76 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_77'] = x_build_parser__mutmut_77 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_78'] = x_build_parser__mutmut_78 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_79'] = x_build_parser__mutmut_79 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_80'] = x_build_parser__mutmut_80 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_81'] = x_build_parser__mutmut_81 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_82'] = x_build_parser__mutmut_82 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_83'] = x_build_parser__mutmut_83 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_84'] = x_build_parser__mutmut_84 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_85'] = x_build_parser__mutmut_85 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_86'] = x_build_parser__mutmut_86 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_87'] = x_build_parser__mutmut_87 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_88'] = x_build_parser__mutmut_88 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_89'] = x_build_parser__mutmut_89 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_90'] = x_build_parser__mutmut_90 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_91'] = x_build_parser__mutmut_91 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_92'] = x_build_parser__mutmut_92 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_93'] = x_build_parser__mutmut_93 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_94'] = x_build_parser__mutmut_94 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_95'] = x_build_parser__mutmut_95 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_96'] = x_build_parser__mutmut_96 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_97'] = x_build_parser__mutmut_97 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_98'] = x_build_parser__mutmut_98 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_99'] = x_build_parser__mutmut_99 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_100'] = x_build_parser__mutmut_100 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_101'] = x_build_parser__mutmut_101 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_102'] = x_build_parser__mutmut_102 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_103'] = x_build_parser__mutmut_103 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_104'] = x_build_parser__mutmut_104 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_105'] = x_build_parser__mutmut_105 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_106'] = x_build_parser__mutmut_106 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_107'] = x_build_parser__mutmut_107 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_108'] = x_build_parser__mutmut_108 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_109'] = x_build_parser__mutmut_109 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_110'] = x_build_parser__mutmut_110 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_111'] = x_build_parser__mutmut_111 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_112'] = x_build_parser__mutmut_112 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_113'] = x_build_parser__mutmut_113 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_114'] = x_build_parser__mutmut_114 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_115'] = x_build_parser__mutmut_115 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_116'] = x_build_parser__mutmut_116 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_117'] = x_build_parser__mutmut_117 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_118'] = x_build_parser__mutmut_118 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_119'] = x_build_parser__mutmut_119 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_120'] = x_build_parser__mutmut_120 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_121'] = x_build_parser__mutmut_121 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_122'] = x_build_parser__mutmut_122 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_123'] = x_build_parser__mutmut_123 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_124'] = x_build_parser__mutmut_124 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_125'] = x_build_parser__mutmut_125 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_126'] = x_build_parser__mutmut_126 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_127'] = x_build_parser__mutmut_127 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_128'] = x_build_parser__mutmut_128 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_129'] = x_build_parser__mutmut_129 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_130'] = x_build_parser__mutmut_130 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_131'] = x_build_parser__mutmut_131 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_132'] = x_build_parser__mutmut_132 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_133'] = x_build_parser__mutmut_133 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_134'] = x_build_parser__mutmut_134 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_135'] = x_build_parser__mutmut_135 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_136'] = x_build_parser__mutmut_136 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_137'] = x_build_parser__mutmut_137 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_138'] = x_build_parser__mutmut_138 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_139'] = x_build_parser__mutmut_139 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_140'] = x_build_parser__mutmut_140 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_141'] = x_build_parser__mutmut_141 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_142'] = x_build_parser__mutmut_142 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_143'] = x_build_parser__mutmut_143 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_144'] = x_build_parser__mutmut_144 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_145'] = x_build_parser__mutmut_145 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_146'] = x_build_parser__mutmut_146 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_147'] = x_build_parser__mutmut_147 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_148'] = x_build_parser__mutmut_148 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_149'] = x_build_parser__mutmut_149 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_150'] = x_build_parser__mutmut_150 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_151'] = x_build_parser__mutmut_151 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_152'] = x_build_parser__mutmut_152 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_153'] = x_build_parser__mutmut_153 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_154'] = x_build_parser__mutmut_154 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_155'] = x_build_parser__mutmut_155 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_156'] = x_build_parser__mutmut_156 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_157'] = x_build_parser__mutmut_157 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_158'] = x_build_parser__mutmut_158 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_159'] = x_build_parser__mutmut_159 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_160'] = x_build_parser__mutmut_160 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_161'] = x_build_parser__mutmut_161 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_162'] = x_build_parser__mutmut_162 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_163'] = x_build_parser__mutmut_163 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_164'] = x_build_parser__mutmut_164 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_165'] = x_build_parser__mutmut_165 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_166'] = x_build_parser__mutmut_166 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_167'] = x_build_parser__mutmut_167 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_168'] = x_build_parser__mutmut_168 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_169'] = x_build_parser__mutmut_169 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_170'] = x_build_parser__mutmut_170 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_171'] = x_build_parser__mutmut_171 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_172'] = x_build_parser__mutmut_172 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_173'] = x_build_parser__mutmut_173 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_174'] = x_build_parser__mutmut_174 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_175'] = x_build_parser__mutmut_175 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_176'] = x_build_parser__mutmut_176 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_177'] = x_build_parser__mutmut_177 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_178'] = x_build_parser__mutmut_178 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_179'] = x_build_parser__mutmut_179 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_180'] = x_build_parser__mutmut_180 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_181'] = x_build_parser__mutmut_181 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_182'] = x_build_parser__mutmut_182 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_183'] = x_build_parser__mutmut_183 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_184'] = x_build_parser__mutmut_184 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_185'] = x_build_parser__mutmut_185 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_186'] = x_build_parser__mutmut_186 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_187'] = x_build_parser__mutmut_187 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_188'] = x_build_parser__mutmut_188 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_189'] = x_build_parser__mutmut_189 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_190'] = x_build_parser__mutmut_190 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_191'] = x_build_parser__mutmut_191 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_192'] = x_build_parser__mutmut_192 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_193'] = x_build_parser__mutmut_193 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_194'] = x_build_parser__mutmut_194 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_195'] = x_build_parser__mutmut_195 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_196'] = x_build_parser__mutmut_196 # type: ignore # mutmut generated
mutants_x_normalize_opt_level__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_normalize_opt_level__mutmut)
def normalize_opt_level(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = opt.strip()
    if s.startswith("-O"):
        return s
    if s.startswith("O"):
        return f"-{s}"
    return f"-O{s}"


def x_normalize_opt_level__mutmut_orig(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = opt.strip()
    if s.startswith("-O"):
        return s
    if s.startswith("O"):
        return f"-{s}"
    return f"-O{s}"


def x_normalize_opt_level__mutmut_1(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = None
    if s.startswith("-O"):
        return s
    if s.startswith("O"):
        return f"-{s}"
    return f"-O{s}"


def x_normalize_opt_level__mutmut_2(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = opt.strip()
    if s.startswith(None):
        return s
    if s.startswith("O"):
        return f"-{s}"
    return f"-O{s}"


def x_normalize_opt_level__mutmut_3(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = opt.strip()
    if s.startswith("XX-OXX"):
        return s
    if s.startswith("O"):
        return f"-{s}"
    return f"-O{s}"


def x_normalize_opt_level__mutmut_4(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = opt.strip()
    if s.startswith("-o"):
        return s
    if s.startswith("O"):
        return f"-{s}"
    return f"-O{s}"


def x_normalize_opt_level__mutmut_5(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = opt.strip()
    if s.startswith("-O"):
        return s
    if s.startswith(None):
        return f"-{s}"
    return f"-O{s}"


def x_normalize_opt_level__mutmut_6(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = opt.strip()
    if s.startswith("-O"):
        return s
    if s.startswith("XXOXX"):
        return f"-{s}"
    return f"-O{s}"


def x_normalize_opt_level__mutmut_7(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = opt.strip()
    if s.startswith("-O"):
        return s
    if s.startswith("o"):
        return f"-{s}"
    return f"-O{s}"

mutants_x_normalize_opt_level__mutmut['_mutmut_orig'] = x_normalize_opt_level__mutmut_orig # type: ignore # mutmut generated
mutants_x_normalize_opt_level__mutmut['x_normalize_opt_level__mutmut_1'] = x_normalize_opt_level__mutmut_1 # type: ignore # mutmut generated
mutants_x_normalize_opt_level__mutmut['x_normalize_opt_level__mutmut_2'] = x_normalize_opt_level__mutmut_2 # type: ignore # mutmut generated
mutants_x_normalize_opt_level__mutmut['x_normalize_opt_level__mutmut_3'] = x_normalize_opt_level__mutmut_3 # type: ignore # mutmut generated
mutants_x_normalize_opt_level__mutmut['x_normalize_opt_level__mutmut_4'] = x_normalize_opt_level__mutmut_4 # type: ignore # mutmut generated
mutants_x_normalize_opt_level__mutmut['x_normalize_opt_level__mutmut_5'] = x_normalize_opt_level__mutmut_5 # type: ignore # mutmut generated
mutants_x_normalize_opt_level__mutmut['x_normalize_opt_level__mutmut_6'] = x_normalize_opt_level__mutmut_6 # type: ignore # mutmut generated
mutants_x_normalize_opt_level__mutmut['x_normalize_opt_level__mutmut_7'] = x_normalize_opt_level__mutmut_7 # type: ignore # mutmut generated
mutants_x_main__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_main__mutmut)
def main(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_orig(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_1(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = None
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_2(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = None

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_3(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(None)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_4(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = None
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_5(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "XXhackXX"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_6(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "HACK"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_7(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = None
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_8(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "XXrawXX"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_9(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "RAW"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_10(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = None

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_11(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "XXcoeXX"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_12(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "COE"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_13(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = None
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_14(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=None, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_15(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=None)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_16(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_17(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, )
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_18(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=None,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_19(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=None,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_20(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=None,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_21(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=None,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_22(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=None,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_23(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=None,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_24(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=None,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_25(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=None,
    )


def x_main__mutmut_26(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_27(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_28(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_29(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_30(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_31(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_32(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_33(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        )


def x_main__mutmut_34(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(None),
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_35(argv: Optional[list[str]] = None) -> int:
    """Main entry point for hcc."""
    parser = build_parser()
    args = parser.parse_args(argv)

    format_type = "hack"
    if args.raw:
        format_type = "raw"
    elif args.coe:
        format_type = "coe"

    driver = CompilerDriver(cc=args.cc, has=args.has)
    return driver.compile_c_to_hack(
        input_c_path=args.input_file,
        output_path=args.outfile,
        format_type=format_type,
        stdout_mode=args.stdout,
        stop_at_asm=args.assemble_only,
        keep_temps=args.keep,
        opt_level=normalize_opt_level(args.opt_level),
        include_crt0=args.no_crt0,
    )

mutants_x_main__mutmut['_mutmut_orig'] = x_main__mutmut_orig # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_1'] = x_main__mutmut_1 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_2'] = x_main__mutmut_2 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_3'] = x_main__mutmut_3 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_4'] = x_main__mutmut_4 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_5'] = x_main__mutmut_5 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_6'] = x_main__mutmut_6 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_7'] = x_main__mutmut_7 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_8'] = x_main__mutmut_8 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_9'] = x_main__mutmut_9 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_10'] = x_main__mutmut_10 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_11'] = x_main__mutmut_11 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_12'] = x_main__mutmut_12 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_13'] = x_main__mutmut_13 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_14'] = x_main__mutmut_14 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_15'] = x_main__mutmut_15 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_16'] = x_main__mutmut_16 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_17'] = x_main__mutmut_17 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_18'] = x_main__mutmut_18 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_19'] = x_main__mutmut_19 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_20'] = x_main__mutmut_20 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_21'] = x_main__mutmut_21 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_22'] = x_main__mutmut_22 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_23'] = x_main__mutmut_23 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_24'] = x_main__mutmut_24 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_25'] = x_main__mutmut_25 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_26'] = x_main__mutmut_26 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_27'] = x_main__mutmut_27 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_28'] = x_main__mutmut_28 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_29'] = x_main__mutmut_29 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_30'] = x_main__mutmut_30 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_31'] = x_main__mutmut_31 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_32'] = x_main__mutmut_32 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_33'] = x_main__mutmut_33 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_34'] = x_main__mutmut_34 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_35'] = x_main__mutmut_35 # type: ignore # mutmut generated


if __name__ == "__main__":
    sys.exit(main())
