# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

"""Command-line interface for hcc (Hack C Compiler frontend)."""

import argparse
import sys
from typing import Optional

from m2h import __version__
from m2h.driver import CompilerDriver


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


def normalize_opt_level(opt: str) -> str:
    """Normalize optimization level string (e.g. '2' -> '-O2', '-O2' -> '-O2')."""
    s = opt.strip()
    if s.startswith("-O"):
        return s
    if s.startswith("O"):
        return f"-{s}"
    return f"-O{s}"


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


if __name__ == "__main__":
    sys.exit(main())
