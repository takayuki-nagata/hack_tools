# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

"""Compiler driver connecting msp430-gcc, m2h, and has."""

import os
import shutil
import subprocess
import sys
import tempfile
from typing import Optional

from m2h.cli import transpile_file


def find_executable(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(name)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) and os.access(fallback, os.X_OK):
                return os.path.abspath(fallback)
    return None


def get_compiler_version_info(cc: str) -> Optional[tuple[int, int, int, str]]:
    """Query compiler version by running `<cc> --version`."""
    try:
        proc = subprocess.run([cc, "--version"], capture_output=True, text=True, check=False)
        output = proc.stdout if proc.stdout else proc.stderr
        if not output:
            return None
        import re

        match = re.search(r"(\d+)\.(\d+)\.(\d+)", output)
        if match:
            major, minor, patch = int(match.group(1)), int(match.group(2)), int(match.group(3))
            first_line = output.splitlines()[0].strip()
            return (major, minor, patch, first_line)
    except Exception:
        pass
    return None


def run_command(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            if proc.stderr:
                sys.stderr.write(proc.stderr)
            elif proc.stdout:
                sys.stderr.write(proc.stdout)
            return proc.returncode
        return 0
    except Exception as e:
        sys.stderr.write(f"hcc: error executing '{cmd[0]}': {e}\n")
        return 1


class CompilerDriver:
    """Orchestrates C compilation -> MSP430 Asm -> Hack Asm -> Hack Binary."""

    def __init__(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc or msp430-elf-gcc
        home_dir = os.path.expanduser("~")
        local_bin = os.path.join(home_dir, ".local", "bin")
        local_toolchain_bin = os.path.join(home_dir, ".local", "msp430-gcc", "bin")
        fallback_ccs = [
            os.path.join(local_bin, "msp430-elf-gcc"),
            os.path.join(local_bin, "msp430-gcc"),
            os.path.join(local_toolchain_bin, "msp430-elf-gcc"),
            os.path.join(local_toolchain_bin, "msp430-gcc"),
        ]
        self.cc = (
            cc
            or find_executable("msp430-elf-gcc", fallback_paths=fallback_ccs)
            or find_executable("msp430-gcc", fallback_paths=fallback_ccs)
            or "msp430-gcc"
        )
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def compile_c_to_hack(
        self,
        input_c_path: str,
        output_path: Optional[str] = None,
        format_type: str = "hack",  # "hack", "raw", "coe"
        stdout_mode: bool = False,
        stop_at_asm: bool = False,
        keep_temps: bool = False,
        opt_level: str = "-O2",
        include_crt0: bool = True,
    ) -> int:
        """Execute the full compilation pipeline."""
        if not os.path.exists(input_c_path):
            sys.stderr.write(f"hcc: error: input file '{input_c_path}' not found\n")
            return 1

        # Check compiler presence
        resolved_cc = shutil.which(self.cc) or (
            self.cc if (os.path.isfile(self.cc) and os.access(self.cc, os.X_OK)) else None
        )
        if not resolved_cc:
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install TI MSP430 GCC "
                "(run 'make install-msp430-gcc' or install gcc-msp430).\n"
            )
            return 1

        # Check compiler version and warn if not recommended version (9.3.1 / 9.x+)
        version_info = get_compiler_version_info(resolved_cc)
        if version_info:
            major, minor, patch_v, _ = version_info
            if major < 9:
                sys.stderr.write(
                    f"hcc: warning: MSP430 GCC version '{major}.{minor}.{patch_v}' detected.\n"
                    "Recommended version is TI MSP430 GCC 9.3.1.11.\n"
                    "Run 'make install-msp430-gcc' to install the recommended toolchain.\n"
                )

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-mcpu=msp430",
                "-mmax-inline-shift=64",
                "-fno-jump-tables",
                "-std=c99",
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-Wall",
                "-Wextra",
                input_c_path,
                "-o",
                s_file,
            ]
            ret = run_command(gcc_cmd)
            if ret != 0:
                sys.stderr.write(f"hcc: compilation failed at gcc stage (code {ret})\n")
                return ret

            # 2. Run m2h transpiler to produce Hack assembly (.asm)
            ret = transpile_file(
                input_path=s_file,
                output_path=asm_file,
                to_stdout=False,
                include_crt0=include_crt0,
            )
            if ret != 0:
                sys.stderr.write(f"hcc: transpilation failed at m2h stage (code {ret})\n")
                return ret

            # If user requested assembly output only (-S)
            if stop_at_asm:
                if stdout_mode:
                    with open(asm_file, encoding="utf-8") as f:
                        sys.stdout.write(f.read())
                    return 0
                target_asm = output_path if output_path else f"{base_name}.asm"
                if asm_file != target_asm:
                    shutil.copyfile(asm_file, target_asm)
                return 0

            # Check has assembler presence
            if not shutil.which(self.has) and not (
                os.path.isfile(self.has) and os.access(self.has, os.X_OK)
            ):
                sys.stderr.write(
                    f"hcc: error: Hack assembler '{self.has}' not found.\n"
                    "Please build 'has' or ensure it is in PATH.\n"
                )
                return 1

            # 3. Run has assembler to produce Hack machine code (.hack / .bin / .coe)
            has_cmd = [self.has]
            if format_type == "raw":
                has_cmd.append("-r")
            elif format_type == "coe":
                has_cmd.append("-c")

            if stdout_mode:
                has_cmd.append("-s")
            elif output_path:
                has_cmd.extend(["-o", output_path])

            has_cmd.append(asm_file)
            ret = run_command(has_cmd)
            if ret != 0:
                sys.stderr.write(f"hcc: assembly failed at has stage (code {ret})\n")
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
