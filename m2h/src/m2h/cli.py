# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

"""Command-line interface for m2h (MSP430 to Hack assembly transpiler)."""

import argparse
import os
import sys
from typing import Optional

from m2h import __version__
from m2h.emitter import HackEmitter
from m2h.parser import parse_assembly


def build_parser() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def derive_outfile_name(infile_name: str) -> str:
    """Derive output .asm filename from input filename."""
    base, _ = os.path.splitext(infile_name)
    return f"{base}.asm"


def transpile_file(
    input_path: str,
    output_path: Optional[str] = None,
    to_stdout: bool = False,
    include_crt0: bool = True,
) -> int:
    """Transpile an MSP430 assembly file to Hack assembly."""
    if not os.path.exists(input_path):
        sys.stderr.write(f"m2h: error: input file '{input_path}' not found\n")
        return 1

    try:
        with open(input_path, encoding="utf-8") as f:
            source = f.read()
    except Exception as e:
        sys.stderr.write(f"m2h: error reading '{input_path}': {e}\n")
        return 1

    try:
        statements = parse_assembly(source)
        emitter = HackEmitter(include_crt0=include_crt0)
        hack_asm = emitter.emit_program(statements)
    except Exception as e:
        sys.stderr.write(f"m2h: error during transpilation: {e}\n")
        return 1

    if to_stdout:
        sys.stdout.write(hack_asm)
        return 0

    target_out = output_path if output_path else derive_outfile_name(input_path)
    try:
        with open(target_out, "w", encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def main(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        to_stdout=args.stdout,
        include_crt0=not args.no_crt0,
    )


if __name__ == "__main__":
    sys.exit(main())
