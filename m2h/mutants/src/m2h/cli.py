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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_parser__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_parser__mutmut)
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


def x_build_parser__mutmut_orig() -> argparse.ArgumentParser:
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


def x_build_parser__mutmut_1() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = None
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


def x_build_parser__mutmut_2() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog=None,
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


def x_build_parser__mutmut_3() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description=None,
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


def x_build_parser__mutmut_4() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
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


def x_build_parser__mutmut_5() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
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


def x_build_parser__mutmut_6() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="XXm2hXX",
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


def x_build_parser__mutmut_7() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="M2H",
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


def x_build_parser__mutmut_8() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="XXTranspile MSP430 assembly (.s) into Hack assembly (.asm).XX",
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


def x_build_parser__mutmut_9() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="transpile msp430 assembly (.s) into hack assembly (.asm).",
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


def x_build_parser__mutmut_10() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="TRANSPILE MSP430 ASSEMBLY (.S) INTO HACK ASSEMBLY (.ASM).",
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


def x_build_parser__mutmut_11() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument(None, metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_12() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar=None, help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_13() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help=None)
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_14() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument(metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_15() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_16() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", )
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_17() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("XXinput_fileXX", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_18() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("INPUT_FILE", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_19() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="XXFILEXX", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_20() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="file", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_21() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="XXMSP430 assembly input file (.s)XX")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_22() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="msp430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_23() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 ASSEMBLY INPUT FILE (.S)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_24() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument(None, "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_25() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", None, metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_26() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar=None, help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_27() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help=None)
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_28() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_29() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_30() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_31() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", )
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_32() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("XX-oXX", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_33() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-O", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_34() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "XX--outfileXX", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_35() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--OUTFILE", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_36() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="XXFILEXX", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_37() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="file", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_38() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="XXOutput Hack assembly fileXX")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_39() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="output hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_40() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="OUTPUT HACK ASSEMBLY FILE")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_41() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        None, "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_42() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", None, action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_43() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action=None, help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_44() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help=None
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_45() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_46() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_47() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_48() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_49() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "XX-sXX", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_50() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-S", "--stdout", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_51() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "XX--stdoutXX", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_52() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--STDOUT", action="store_true", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_53() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="XXstore_trueXX", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_54() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="STORE_TRUE", help="Output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_55() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="XXOutput to stdout instead of a fileXX"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_56() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="output to stdout instead of a file"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_57() -> argparse.ArgumentParser:
    """Build argument parser for m2h."""
    parser = argparse.ArgumentParser(
        prog="m2h",
        description="Transpile MSP430 assembly (.s) into Hack assembly (.asm).",
    )
    parser.add_argument("input_file", metavar="FILE", help="MSP430 assembly input file (.s)")
    parser.add_argument("-o", "--outfile", metavar="FILE", help="Output Hack assembly file")
    parser.add_argument(
        "-s", "--stdout", action="store_true", help="OUTPUT TO STDOUT INSTEAD OF A FILE"
    )
    parser.add_argument(
        "--no-crt0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_58() -> argparse.ArgumentParser:
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
        None, action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_59() -> argparse.ArgumentParser:
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
        "--no-crt0", action=None, help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_60() -> argparse.ArgumentParser:
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
        "--no-crt0", action="store_true", help=None
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_61() -> argparse.ArgumentParser:
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
        action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_62() -> argparse.ArgumentParser:
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
        "--no-crt0", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_63() -> argparse.ArgumentParser:
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
        "--no-crt0", action="store_true", )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_64() -> argparse.ArgumentParser:
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
        "XX--no-crt0XX", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_65() -> argparse.ArgumentParser:
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
        "--NO-CRT0", action="store_true", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_66() -> argparse.ArgumentParser:
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
        "--no-crt0", action="XXstore_trueXX", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_67() -> argparse.ArgumentParser:
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
        "--no-crt0", action="STORE_TRUE", help="Do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_68() -> argparse.ArgumentParser:
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
        "--no-crt0", action="store_true", help="XXDo not include startup runtime (crt0)XX"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_69() -> argparse.ArgumentParser:
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
        "--no-crt0", action="store_true", help="do not include startup runtime (crt0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_70() -> argparse.ArgumentParser:
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
        "--no-crt0", action="store_true", help="DO NOT INCLUDE STARTUP RUNTIME (CRT0)"
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_71() -> argparse.ArgumentParser:
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
    parser.add_argument(None, "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_72() -> argparse.ArgumentParser:
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
    parser.add_argument("-v", None, action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_73() -> argparse.ArgumentParser:
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
    parser.add_argument("-v", "--version", action=None, version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_74() -> argparse.ArgumentParser:
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
    parser.add_argument("-v", "--version", action="version", version=None)
    return parser


def x_build_parser__mutmut_75() -> argparse.ArgumentParser:
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
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_76() -> argparse.ArgumentParser:
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
    parser.add_argument("-v", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_77() -> argparse.ArgumentParser:
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
    parser.add_argument("-v", "--version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_78() -> argparse.ArgumentParser:
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
    parser.add_argument("-v", "--version", action="version", )
    return parser


def x_build_parser__mutmut_79() -> argparse.ArgumentParser:
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
    parser.add_argument("XX-vXX", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_80() -> argparse.ArgumentParser:
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
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_81() -> argparse.ArgumentParser:
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
    parser.add_argument("-v", "XX--versionXX", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_82() -> argparse.ArgumentParser:
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
    parser.add_argument("-v", "--VERSION", action="version", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_83() -> argparse.ArgumentParser:
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
    parser.add_argument("-v", "--version", action="XXversionXX", version=f"%(prog)s {__version__}")
    return parser


def x_build_parser__mutmut_84() -> argparse.ArgumentParser:
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
mutants_x_derive_outfile_name__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_derive_outfile_name__mutmut)
def derive_outfile_name(infile_name: str) -> str:
    """Derive output .asm filename from input filename."""
    base, _ = os.path.splitext(infile_name)
    return f"{base}.asm"


def x_derive_outfile_name__mutmut_orig(infile_name: str) -> str:
    """Derive output .asm filename from input filename."""
    base, _ = os.path.splitext(infile_name)
    return f"{base}.asm"


def x_derive_outfile_name__mutmut_1(infile_name: str) -> str:
    """Derive output .asm filename from input filename."""
    base, _ = None
    return f"{base}.asm"


def x_derive_outfile_name__mutmut_2(infile_name: str) -> str:
    """Derive output .asm filename from input filename."""
    base, _ = os.path.splitext(None)
    return f"{base}.asm"

mutants_x_derive_outfile_name__mutmut['_mutmut_orig'] = x_derive_outfile_name__mutmut_orig # type: ignore # mutmut generated
mutants_x_derive_outfile_name__mutmut['x_derive_outfile_name__mutmut_1'] = x_derive_outfile_name__mutmut_1 # type: ignore # mutmut generated
mutants_x_derive_outfile_name__mutmut['x_derive_outfile_name__mutmut_2'] = x_derive_outfile_name__mutmut_2 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_transpile_file__mutmut)
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


def x_transpile_file__mutmut_orig(
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


def x_transpile_file__mutmut_1(
    input_path: str,
    output_path: Optional[str] = None,
    to_stdout: bool = True,
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


def x_transpile_file__mutmut_2(
    input_path: str,
    output_path: Optional[str] = None,
    to_stdout: bool = False,
    include_crt0: bool = False,
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


def x_transpile_file__mutmut_3(
    input_path: str,
    output_path: Optional[str] = None,
    to_stdout: bool = False,
    include_crt0: bool = True,
) -> int:
    """Transpile an MSP430 assembly file to Hack assembly."""
    if os.path.exists(input_path):
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


def x_transpile_file__mutmut_4(
    input_path: str,
    output_path: Optional[str] = None,
    to_stdout: bool = False,
    include_crt0: bool = True,
) -> int:
    """Transpile an MSP430 assembly file to Hack assembly."""
    if not os.path.exists(None):
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


def x_transpile_file__mutmut_5(
    input_path: str,
    output_path: Optional[str] = None,
    to_stdout: bool = False,
    include_crt0: bool = True,
) -> int:
    """Transpile an MSP430 assembly file to Hack assembly."""
    if not os.path.exists(input_path):
        sys.stderr.write(None)
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


def x_transpile_file__mutmut_6(
    input_path: str,
    output_path: Optional[str] = None,
    to_stdout: bool = False,
    include_crt0: bool = True,
) -> int:
    """Transpile an MSP430 assembly file to Hack assembly."""
    if not os.path.exists(input_path):
        sys.stderr.write(f"m2h: error: input file '{input_path}' not found\n")
        return 2

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


def x_transpile_file__mutmut_7(
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
        with open(None, encoding="utf-8") as f:
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


def x_transpile_file__mutmut_8(
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
        with open(input_path, encoding=None) as f:
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


def x_transpile_file__mutmut_9(
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
        with open(encoding="utf-8") as f:
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


def x_transpile_file__mutmut_10(
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
        with open(input_path, ) as f:
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


def x_transpile_file__mutmut_11(
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
        with open(input_path, encoding="XXutf-8XX") as f:
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


def x_transpile_file__mutmut_12(
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
        with open(input_path, encoding="UTF-8") as f:
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


def x_transpile_file__mutmut_13(
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
            source = None
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


def x_transpile_file__mutmut_14(
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
        sys.stderr.write(None)
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


def x_transpile_file__mutmut_15(
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
        return 2

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


def x_transpile_file__mutmut_16(
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
        statements = None
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


def x_transpile_file__mutmut_17(
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
        statements = parse_assembly(None)
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


def x_transpile_file__mutmut_18(
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
        emitter = None
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


def x_transpile_file__mutmut_19(
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
        emitter = HackEmitter(include_crt0=None)
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


def x_transpile_file__mutmut_20(
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
        hack_asm = None
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


def x_transpile_file__mutmut_21(
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
        hack_asm = emitter.emit_program(None)
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


def x_transpile_file__mutmut_22(
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
        sys.stderr.write(None)
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


def x_transpile_file__mutmut_23(
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
        return 2

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


def x_transpile_file__mutmut_24(
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
        sys.stdout.write(None)
        return 0

    target_out = output_path if output_path else derive_outfile_name(input_path)
    try:
        with open(target_out, "w", encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_25(
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
        return 1

    target_out = output_path if output_path else derive_outfile_name(input_path)
    try:
        with open(target_out, "w", encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_26(
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

    target_out = None
    try:
        with open(target_out, "w", encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_27(
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

    target_out = output_path if output_path else derive_outfile_name(None)
    try:
        with open(target_out, "w", encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_28(
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
        with open(None, "w", encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_29(
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
        with open(target_out, None, encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_30(
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
        with open(target_out, "w", encoding=None) as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_31(
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
        with open("w", encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_32(
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
        with open(target_out, encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_33(
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
        with open(target_out, "w", ) as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_34(
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
        with open(target_out, "XXwXX", encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_35(
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
        with open(target_out, "W", encoding="utf-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_36(
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
        with open(target_out, "w", encoding="XXutf-8XX") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_37(
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
        with open(target_out, "w", encoding="UTF-8") as f:
            f.write(hack_asm)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_38(
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
            f.write(None)
    except Exception as e:
        sys.stderr.write(f"m2h: error writing to '{target_out}': {e}\n")
        return 1

    return 0


def x_transpile_file__mutmut_39(
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
        sys.stderr.write(None)
        return 1

    return 0


def x_transpile_file__mutmut_40(
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
        return 2

    return 0


def x_transpile_file__mutmut_41(
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

    return 1

mutants_x_transpile_file__mutmut['_mutmut_orig'] = x_transpile_file__mutmut_orig # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_1'] = x_transpile_file__mutmut_1 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_2'] = x_transpile_file__mutmut_2 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_3'] = x_transpile_file__mutmut_3 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_4'] = x_transpile_file__mutmut_4 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_5'] = x_transpile_file__mutmut_5 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_6'] = x_transpile_file__mutmut_6 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_7'] = x_transpile_file__mutmut_7 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_8'] = x_transpile_file__mutmut_8 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_9'] = x_transpile_file__mutmut_9 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_10'] = x_transpile_file__mutmut_10 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_11'] = x_transpile_file__mutmut_11 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_12'] = x_transpile_file__mutmut_12 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_13'] = x_transpile_file__mutmut_13 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_14'] = x_transpile_file__mutmut_14 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_15'] = x_transpile_file__mutmut_15 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_16'] = x_transpile_file__mutmut_16 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_17'] = x_transpile_file__mutmut_17 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_18'] = x_transpile_file__mutmut_18 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_19'] = x_transpile_file__mutmut_19 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_20'] = x_transpile_file__mutmut_20 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_21'] = x_transpile_file__mutmut_21 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_22'] = x_transpile_file__mutmut_22 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_23'] = x_transpile_file__mutmut_23 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_24'] = x_transpile_file__mutmut_24 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_25'] = x_transpile_file__mutmut_25 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_26'] = x_transpile_file__mutmut_26 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_27'] = x_transpile_file__mutmut_27 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_28'] = x_transpile_file__mutmut_28 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_29'] = x_transpile_file__mutmut_29 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_30'] = x_transpile_file__mutmut_30 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_31'] = x_transpile_file__mutmut_31 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_32'] = x_transpile_file__mutmut_32 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_33'] = x_transpile_file__mutmut_33 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_34'] = x_transpile_file__mutmut_34 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_35'] = x_transpile_file__mutmut_35 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_36'] = x_transpile_file__mutmut_36 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_37'] = x_transpile_file__mutmut_37 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_38'] = x_transpile_file__mutmut_38 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_39'] = x_transpile_file__mutmut_39 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_40'] = x_transpile_file__mutmut_40 # type: ignore # mutmut generated
mutants_x_transpile_file__mutmut['x_transpile_file__mutmut_41'] = x_transpile_file__mutmut_41 # type: ignore # mutmut generated
mutants_x_main__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_main__mutmut)
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


def x_main__mutmut_orig(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        to_stdout=args.stdout,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_1(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = None
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        to_stdout=args.stdout,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_2(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = None

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        to_stdout=args.stdout,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_3(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(None)

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        to_stdout=args.stdout,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_4(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=None,
        output_path=args.outfile,
        to_stdout=args.stdout,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_5(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        output_path=None,
        to_stdout=args.stdout,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_6(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        to_stdout=None,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_7(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        to_stdout=args.stdout,
        include_crt0=None,
    )


def x_main__mutmut_8(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        output_path=args.outfile,
        to_stdout=args.stdout,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_9(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        to_stdout=args.stdout,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_10(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        include_crt0=not args.no_crt0,
    )


def x_main__mutmut_11(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        to_stdout=args.stdout,
        )


def x_main__mutmut_12(argv: Optional[list[str]] = None) -> int:
    """Main CLI entry point for m2h."""
    parser = build_parser()
    args = parser.parse_args(argv)

    return transpile_file(
        input_path=args.input_file,
        output_path=args.outfile,
        to_stdout=args.stdout,
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


if __name__ == "__main__":
    sys.exit(main())
