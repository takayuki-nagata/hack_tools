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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_find_executable__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_executable__mutmut)
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


def x_find_executable__mutmut_orig(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(name)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) and os.access(fallback, os.X_OK):
                return os.path.abspath(fallback)
    return None


def x_find_executable__mutmut_1(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = None
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) and os.access(fallback, os.X_OK):
                return os.path.abspath(fallback)
    return None


def x_find_executable__mutmut_2(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(None)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) and os.access(fallback, os.X_OK):
                return os.path.abspath(fallback)
    return None


def x_find_executable__mutmut_3(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(name)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) or os.access(fallback, os.X_OK):
                return os.path.abspath(fallback)
    return None


def x_find_executable__mutmut_4(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(name)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(None) and os.access(fallback, os.X_OK):
                return os.path.abspath(fallback)
    return None


def x_find_executable__mutmut_5(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(name)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) and os.access(None, os.X_OK):
                return os.path.abspath(fallback)
    return None


def x_find_executable__mutmut_6(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(name)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) and os.access(fallback, None):
                return os.path.abspath(fallback)
    return None


def x_find_executable__mutmut_7(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(name)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) and os.access(os.X_OK):
                return os.path.abspath(fallback)
    return None


def x_find_executable__mutmut_8(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(name)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) and os.access(fallback, ):
                return os.path.abspath(fallback)
    return None


def x_find_executable__mutmut_9(name: str, fallback_paths: Optional[list[str]] = None) -> Optional[str]:
    """Find an executable in PATH or fallback locations."""
    path = shutil.which(name)
    if path:
        return path
    if fallback_paths:
        for fallback in fallback_paths:
            if os.path.isfile(fallback) and os.access(fallback, os.X_OK):
                return os.path.abspath(None)
    return None

mutants_x_find_executable__mutmut['_mutmut_orig'] = x_find_executable__mutmut_orig # type: ignore # mutmut generated
mutants_x_find_executable__mutmut['x_find_executable__mutmut_1'] = x_find_executable__mutmut_1 # type: ignore # mutmut generated
mutants_x_find_executable__mutmut['x_find_executable__mutmut_2'] = x_find_executable__mutmut_2 # type: ignore # mutmut generated
mutants_x_find_executable__mutmut['x_find_executable__mutmut_3'] = x_find_executable__mutmut_3 # type: ignore # mutmut generated
mutants_x_find_executable__mutmut['x_find_executable__mutmut_4'] = x_find_executable__mutmut_4 # type: ignore # mutmut generated
mutants_x_find_executable__mutmut['x_find_executable__mutmut_5'] = x_find_executable__mutmut_5 # type: ignore # mutmut generated
mutants_x_find_executable__mutmut['x_find_executable__mutmut_6'] = x_find_executable__mutmut_6 # type: ignore # mutmut generated
mutants_x_find_executable__mutmut['x_find_executable__mutmut_7'] = x_find_executable__mutmut_7 # type: ignore # mutmut generated
mutants_x_find_executable__mutmut['x_find_executable__mutmut_8'] = x_find_executable__mutmut_8 # type: ignore # mutmut generated
mutants_x_find_executable__mutmut['x_find_executable__mutmut_9'] = x_find_executable__mutmut_9 # type: ignore # mutmut generated
mutants_x_run_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_run_command__mutmut)
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


def x_run_command__mutmut_orig(cmd: list[str]) -> int:
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


def x_run_command__mutmut_1(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = None
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


def x_run_command__mutmut_2(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(None, capture_output=True, text=True, check=False)
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


def x_run_command__mutmut_3(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=None, text=True, check=False)
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


def x_run_command__mutmut_4(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=None, check=False)
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


def x_run_command__mutmut_5(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=None)
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


def x_run_command__mutmut_6(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(capture_output=True, text=True, check=False)
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


def x_run_command__mutmut_7(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, text=True, check=False)
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


def x_run_command__mutmut_8(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, check=False)
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


def x_run_command__mutmut_9(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, )
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


def x_run_command__mutmut_10(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=False, text=True, check=False)
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


def x_run_command__mutmut_11(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=False, check=False)
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


def x_run_command__mutmut_12(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
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


def x_run_command__mutmut_13(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode == 0:
            if proc.stderr:
                sys.stderr.write(proc.stderr)
            elif proc.stdout:
                sys.stderr.write(proc.stdout)
            return proc.returncode
        return 0
    except Exception as e:
        sys.stderr.write(f"hcc: error executing '{cmd[0]}': {e}\n")
        return 1


def x_run_command__mutmut_14(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode != 1:
            if proc.stderr:
                sys.stderr.write(proc.stderr)
            elif proc.stdout:
                sys.stderr.write(proc.stdout)
            return proc.returncode
        return 0
    except Exception as e:
        sys.stderr.write(f"hcc: error executing '{cmd[0]}': {e}\n")
        return 1


def x_run_command__mutmut_15(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            if proc.stderr:
                sys.stderr.write(None)
            elif proc.stdout:
                sys.stderr.write(proc.stdout)
            return proc.returncode
        return 0
    except Exception as e:
        sys.stderr.write(f"hcc: error executing '{cmd[0]}': {e}\n")
        return 1


def x_run_command__mutmut_16(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            if proc.stderr:
                sys.stderr.write(proc.stderr)
            elif proc.stdout:
                sys.stderr.write(None)
            return proc.returncode
        return 0
    except Exception as e:
        sys.stderr.write(f"hcc: error executing '{cmd[0]}': {e}\n")
        return 1


def x_run_command__mutmut_17(cmd: list[str]) -> int:
    """Run a subprocess command and stream stderr on failure."""
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            if proc.stderr:
                sys.stderr.write(proc.stderr)
            elif proc.stdout:
                sys.stderr.write(proc.stdout)
            return proc.returncode
        return 1
    except Exception as e:
        sys.stderr.write(f"hcc: error executing '{cmd[0]}': {e}\n")
        return 1


def x_run_command__mutmut_18(cmd: list[str]) -> int:
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
        sys.stderr.write(None)
        return 1


def x_run_command__mutmut_19(cmd: list[str]) -> int:
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
        sys.stderr.write(f"hcc: error executing '{cmd[1]}': {e}\n")
        return 1


def x_run_command__mutmut_20(cmd: list[str]) -> int:
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
        return 2

mutants_x_run_command__mutmut['_mutmut_orig'] = x_run_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_1'] = x_run_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_2'] = x_run_command__mutmut_2 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_3'] = x_run_command__mutmut_3 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_4'] = x_run_command__mutmut_4 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_5'] = x_run_command__mutmut_5 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_6'] = x_run_command__mutmut_6 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_7'] = x_run_command__mutmut_7 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_8'] = x_run_command__mutmut_8 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_9'] = x_run_command__mutmut_9 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_10'] = x_run_command__mutmut_10 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_11'] = x_run_command__mutmut_11 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_12'] = x_run_command__mutmut_12 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_13'] = x_run_command__mutmut_13 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_14'] = x_run_command__mutmut_14 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_15'] = x_run_command__mutmut_15 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_16'] = x_run_command__mutmut_16 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_17'] = x_run_command__mutmut_17 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_18'] = x_run_command__mutmut_18 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_19'] = x_run_command__mutmut_19 # type: ignore # mutmut generated
mutants_x_run_command__mutmut['x_run_command__mutmut_20'] = x_run_command__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut: MutantDict = {}  # type: ignore


class CompilerDriver:
    """Orchestrates C compilation -> MSP430 Asm -> Hack Asm -> Hack Binary."""

    @_mutmut_mutated(mutants_xǁCompilerDriverǁ__init____mutmut)
    def __init__(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_orig(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_1(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = None
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_2(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") and "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_3(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc and find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_4(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable(None) or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_5(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("XXmsp430-gccXX") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_6(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("MSP430-GCC") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_7(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "XXmsp430-gccXX"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_8(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "MSP430-GCC"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_9(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = None
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_10(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(None)
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_11(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(None))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_12(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = None
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_13(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(None)
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_14(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(None, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_15(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, None, "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_16(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", None, ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_17(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", None))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_18(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join("..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_19(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_20(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_21(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_22(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "XX..XX", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_23(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "XX..XX", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_24(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", "XX..XX"))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_25(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = None
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_26(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(None, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_27(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, None, "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_28(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", None)
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_29(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join("has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_30(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_31(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", )
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_32(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "XXhasXX", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_33(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "HAS", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_34(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "XXhasXX")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_35(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "HAS")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_36(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = None

    def xǁCompilerDriverǁ__init____mutmut_37(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) and "has"

    def xǁCompilerDriverǁ__init____mutmut_38(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has and find_executable("has", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_39(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable(None, fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_40(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=None) or "has"

    def xǁCompilerDriverǁ__init____mutmut_41(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable(fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_42(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", ) or "has"

    def xǁCompilerDriverǁ__init____mutmut_43(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("XXhasXX", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_44(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("HAS", fallback_paths=[local_has]) or "has"

    def xǁCompilerDriverǁ__init____mutmut_45(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "XXhasXX"

    def xǁCompilerDriverǁ__init____mutmut_46(
        self,
        cc: Optional[str] = None,
        has: Optional[str] = None,
    ) -> None:
        # Resolve msp430-gcc
        self.cc = cc or find_executable("msp430-gcc") or "msp430-gcc"
        # Resolve has
        # Check current directory / relative paths for builtin has
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        local_has = os.path.join(repo_root, "has", "has")
        self.has = has or find_executable("has", fallback_paths=[local_has]) or "HAS"

    @_mutmut_mutated(mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut)
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_orig(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_1(
        self,
        input_c_path: str,
        output_path: Optional[str] = None,
        format_type: str = "XXhackXX",  # "hack", "raw", "coe"
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_2(
        self,
        input_c_path: str,
        output_path: Optional[str] = None,
        format_type: str = "HACK",  # "hack", "raw", "coe"
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_3(
        self,
        input_c_path: str,
        output_path: Optional[str] = None,
        format_type: str = "hack",  # "hack", "raw", "coe"
        stdout_mode: bool = True,
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_4(
        self,
        input_c_path: str,
        output_path: Optional[str] = None,
        format_type: str = "hack",  # "hack", "raw", "coe"
        stdout_mode: bool = False,
        stop_at_asm: bool = True,
        keep_temps: bool = False,
        opt_level: str = "-O2",
        include_crt0: bool = True,
    ) -> int:
        """Execute the full compilation pipeline."""
        if not os.path.exists(input_c_path):
            sys.stderr.write(f"hcc: error: input file '{input_c_path}' not found\n")
            return 1

        # Check compiler presence
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_5(
        self,
        input_c_path: str,
        output_path: Optional[str] = None,
        format_type: str = "hack",  # "hack", "raw", "coe"
        stdout_mode: bool = False,
        stop_at_asm: bool = False,
        keep_temps: bool = True,
        opt_level: str = "-O2",
        include_crt0: bool = True,
    ) -> int:
        """Execute the full compilation pipeline."""
        if not os.path.exists(input_c_path):
            sys.stderr.write(f"hcc: error: input file '{input_c_path}' not found\n")
            return 1

        # Check compiler presence
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_6(
        self,
        input_c_path: str,
        output_path: Optional[str] = None,
        format_type: str = "hack",  # "hack", "raw", "coe"
        stdout_mode: bool = False,
        stop_at_asm: bool = False,
        keep_temps: bool = False,
        opt_level: str = "XX-O2XX",
        include_crt0: bool = True,
    ) -> int:
        """Execute the full compilation pipeline."""
        if not os.path.exists(input_c_path):
            sys.stderr.write(f"hcc: error: input file '{input_c_path}' not found\n")
            return 1

        # Check compiler presence
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_7(
        self,
        input_c_path: str,
        output_path: Optional[str] = None,
        format_type: str = "hack",  # "hack", "raw", "coe"
        stdout_mode: bool = False,
        stop_at_asm: bool = False,
        keep_temps: bool = False,
        opt_level: str = "-o2",
        include_crt0: bool = True,
    ) -> int:
        """Execute the full compilation pipeline."""
        if not os.path.exists(input_c_path):
            sys.stderr.write(f"hcc: error: input file '{input_c_path}' not found\n")
            return 1

        # Check compiler presence
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_8(
        self,
        input_c_path: str,
        output_path: Optional[str] = None,
        format_type: str = "hack",  # "hack", "raw", "coe"
        stdout_mode: bool = False,
        stop_at_asm: bool = False,
        keep_temps: bool = False,
        opt_level: str = "-O2",
        include_crt0: bool = False,
    ) -> int:
        """Execute the full compilation pipeline."""
        if not os.path.exists(input_c_path):
            sys.stderr.write(f"hcc: error: input file '{input_c_path}' not found\n")
            return 1

        # Check compiler presence
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_9(
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
        if os.path.exists(input_c_path):
            sys.stderr.write(f"hcc: error: input file '{input_c_path}' not found\n")
            return 1

        # Check compiler presence
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_10(
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
        if not os.path.exists(None):
            sys.stderr.write(f"hcc: error: input file '{input_c_path}' not found\n")
            return 1

        # Check compiler presence
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_11(
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
            sys.stderr.write(None)
            return 1

        # Check compiler presence
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_12(
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
            return 2

        # Check compiler presence
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_13(
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
        if shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_14(
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
        if not shutil.which(None):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_15(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                None
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_16(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "XXPlease install gcc-msp430 XX"
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_17(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_18(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "PLEASE INSTALL GCC-MSP430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_19(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "XX(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\nXX"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_20(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(E.G. 'SUDO APT INSTALL GCC-MSP430' OR 'SUDO DNF INSTALL MSP430-GCC').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_21(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 2

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_22(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = None
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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_23(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(None)
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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_24(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = None

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_25(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix=None)

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_26(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="XXhcc_XX")

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_27(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="HCC_")

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_28(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = None
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_29(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(None, "temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_30(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, None)
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_31(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join("temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_32(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, )
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_33(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "XXtemp.sXX")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_34(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "TEMP.S")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_35(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "temp.s")
            asm_file = None

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_36(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps and stop_at_asm)
                else os.path.join(temp_dir, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_37(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(None, "temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_38(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, None)
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_39(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join("temp.asm")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_40(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, )
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_41(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "XXtemp.asmXX")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_42(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

        base_name, _ = os.path.splitext(input_c_path)
        temp_dir = tempfile.mkdtemp(prefix="hcc_")

        try:
            s_file = f"{base_name}.s" if keep_temps else os.path.join(temp_dir, "temp.s")
            asm_file = (
                f"{base_name}.asm"
                if (keep_temps or stop_at_asm)
                else os.path.join(temp_dir, "TEMP.ASM")
            )

            # 1. Run msp430-gcc to produce MSP430 assembly (.s)
            gcc_cmd = [
                self.cc,
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_43(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
            gcc_cmd = None
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_44(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "XX-SXX",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_45(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-s",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_46(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "XX-ffreestandingXX",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_47(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-FFREESTANDING",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_48(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "XX-fno-asynchronous-unwind-tablesXX",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_49(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-FNO-ASYNCHRONOUS-UNWIND-TABLES",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_50(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "XX-fno-exceptionsXX",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_51(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-FNO-EXCEPTIONS",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_52(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "XX-fno-builtinXX",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_53(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-FNO-BUILTIN",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_54(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "XX-nostdlibXX",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_55(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-NOSTDLIB",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_56(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "XX-mhwmult=noneXX",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_57(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-MHWMULT=NONE",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_58(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "XX-WallXX",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_59(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-wall",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_60(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-WALL",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_61(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "XX-WextraXX",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_62(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "-wextra",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_63(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "-WEXTRA",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_64(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "-Wextra",
                input_c_path,
                "XX-oXX",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_65(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "-Wextra",
                input_c_path,
                "-O",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_66(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "-Wextra",
                input_c_path,
                "-o",
                s_file,
            ]
            ret = None
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_67(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "-Wextra",
                input_c_path,
                "-o",
                s_file,
            ]
            ret = run_command(None)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_68(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "-Wextra",
                input_c_path,
                "-o",
                s_file,
            ]
            ret = run_command(gcc_cmd)
            if ret == 0:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_69(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "-Wextra",
                input_c_path,
                "-o",
                s_file,
            ]
            ret = run_command(gcc_cmd)
            if ret != 1:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_70(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
                "-Wall",
                "-Wextra",
                input_c_path,
                "-o",
                s_file,
            ]
            ret = run_command(gcc_cmd)
            if ret != 0:
                sys.stderr.write(None)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_71(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            ret = None
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_72(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                input_path=None,
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_73(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                output_path=None,
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_74(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                to_stdout=None,
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_75(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                include_crt0=None,
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_76(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_77(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_78(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_79(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_80(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                to_stdout=True,
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_81(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if ret == 0:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_82(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if ret != 1:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_83(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                sys.stderr.write(None)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_84(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    with open(None, encoding="utf-8") as f:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_85(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    with open(asm_file, encoding=None) as f:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_86(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    with open(encoding="utf-8") as f:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_87(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    with open(asm_file, ) as f:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_88(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    with open(asm_file, encoding="XXutf-8XX") as f:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_89(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    with open(asm_file, encoding="UTF-8") as f:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_90(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                        sys.stdout.write(None)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_91(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    return 1
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_92(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                target_asm = None
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_93(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                if asm_file == target_asm:
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_94(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    shutil.copyfile(None, target_asm)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_95(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    shutil.copyfile(asm_file, None)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_96(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    shutil.copyfile(target_asm)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_97(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    shutil.copyfile(asm_file, )
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_98(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                return 1

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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_99(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if not shutil.which(self.has) or not (
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_100(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if shutil.which(self.has) and not (
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_101(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if not shutil.which(None) and not (
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_102(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if not shutil.which(self.has) and (
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_103(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                os.path.isfile(self.has) or os.access(self.has, os.X_OK)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_104(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                os.path.isfile(None) and os.access(self.has, os.X_OK)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_105(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                os.path.isfile(self.has) and os.access(None, os.X_OK)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_106(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                os.path.isfile(self.has) and os.access(self.has, None)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_107(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                os.path.isfile(self.has) and os.access(os.X_OK)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_108(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                os.path.isfile(self.has) and os.access(self.has, )
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_109(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    None
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_110(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    "XXPlease build 'has' or ensure it is in PATH.\nXX"
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_111(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    "please build 'has' or ensure it is in path.\n"
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_112(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                    "PLEASE BUILD 'HAS' OR ENSURE IT IS IN PATH.\n"
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_113(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                return 2

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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_114(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            has_cmd = None
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_115(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if format_type != "raw":
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_116(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if format_type == "XXrawXX":
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_117(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if format_type == "RAW":
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_118(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.append(None)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_119(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.append("XX-rXX")
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_120(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.append("-R")
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_121(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            elif format_type != "coe":
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_122(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            elif format_type == "XXcoeXX":
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_123(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            elif format_type == "COE":
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_124(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.append(None)

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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_125(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.append("XX-cXX")

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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_126(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.append("-C")

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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_127(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.append(None)
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_128(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.append("XX-sXX")
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_129(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.append("-S")
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

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_130(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.extend(None)

            has_cmd.append(asm_file)
            ret = run_command(has_cmd)
            if ret != 0:
                sys.stderr.write(f"hcc: assembly failed at has stage (code {ret})\n")
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_131(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.extend(["XX-oXX", output_path])

            has_cmd.append(asm_file)
            ret = run_command(has_cmd)
            if ret != 0:
                sys.stderr.write(f"hcc: assembly failed at has stage (code {ret})\n")
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_132(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                has_cmd.extend(["-O", output_path])

            has_cmd.append(asm_file)
            ret = run_command(has_cmd)
            if ret != 0:
                sys.stderr.write(f"hcc: assembly failed at has stage (code {ret})\n")
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_133(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

            has_cmd.append(None)
            ret = run_command(has_cmd)
            if ret != 0:
                sys.stderr.write(f"hcc: assembly failed at has stage (code {ret})\n")
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_134(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            ret = None
            if ret != 0:
                sys.stderr.write(f"hcc: assembly failed at has stage (code {ret})\n")
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_135(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            ret = run_command(None)
            if ret != 0:
                sys.stderr.write(f"hcc: assembly failed at has stage (code {ret})\n")
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_136(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if ret == 0:
                sys.stderr.write(f"hcc: assembly failed at has stage (code {ret})\n")
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_137(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if ret != 1:
                sys.stderr.write(f"hcc: assembly failed at has stage (code {ret})\n")
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_138(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                sys.stderr.write(None)
                return ret

            return 0

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_139(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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

            return 1

        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_140(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
            if os.path.exists(None):
                shutil.rmtree(temp_dir)

    def xǁCompilerDriverǁcompile_c_to_hack__mutmut_141(
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
        if not shutil.which(self.cc):
            sys.stderr.write(
                f"hcc: error: MSP430 C compiler '{self.cc}' not found in PATH.\n"
                "Please install gcc-msp430 "
                "(e.g. 'sudo apt install gcc-msp430' or 'sudo dnf install msp430-gcc').\n"
            )
            return 1

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
                "-S",
                opt_level,
                "-ffreestanding",
                "-fno-asynchronous-unwind-tables",
                "-fno-exceptions",
                "-fno-builtin",
                "-nostdlib",
                "-mhwmult=none",
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
                shutil.rmtree(None)

mutants_xǁCompilerDriverǁ__init____mutmut['_mutmut_orig'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_1'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_2'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_3'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_4'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_5'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_6'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_7'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_8'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_9'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_10'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_11'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_12'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_13'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_14'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_15'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_16'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_17'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_18'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_19'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_20'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_21'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_22'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_23'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_24'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_25'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_26'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_27'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_28'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_28 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_29'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_29 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_30'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_30 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_31'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_31 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_32'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_32 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_33'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_33 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_34'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_34 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_35'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_35 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_36'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_36 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_37'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_37 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_38'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_38 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_39'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_39 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_40'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_40 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_41'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_41 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_42'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_42 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_43'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_43 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_44'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_44 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_45'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_45 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁ__init____mutmut['xǁCompilerDriverǁ__init____mutmut_46'] = CompilerDriver.xǁCompilerDriverǁ__init____mutmut_46 # type: ignore # mutmut generated

mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['_mutmut_orig'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_1'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_2'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_3'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_4'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_5'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_6'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_7'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_8'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_9'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_10'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_11'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_12'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_13'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_14'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_15'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_16'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_17'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_18'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_19'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_20'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_21'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_22'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_23'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_24'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_25'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_26'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_27'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_28'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_29'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_30'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_31'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_32'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_33'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_34'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_35'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_36'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_37'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_38'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_39'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_40'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_41'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_42'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_43'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_44'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_45'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_45 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_46'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_46 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_47'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_47 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_48'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_48 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_49'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_49 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_50'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_50 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_51'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_51 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_52'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_52 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_53'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_53 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_54'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_54 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_55'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_55 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_56'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_56 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_57'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_57 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_58'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_58 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_59'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_59 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_60'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_60 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_61'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_61 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_62'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_62 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_63'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_63 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_64'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_64 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_65'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_65 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_66'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_66 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_67'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_67 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_68'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_68 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_69'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_69 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_70'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_70 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_71'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_71 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_72'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_72 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_73'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_73 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_74'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_74 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_75'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_75 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_76'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_76 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_77'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_77 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_78'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_78 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_79'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_79 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_80'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_80 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_81'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_81 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_82'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_82 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_83'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_83 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_84'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_84 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_85'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_85 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_86'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_86 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_87'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_87 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_88'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_88 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_89'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_89 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_90'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_90 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_91'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_91 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_92'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_92 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_93'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_93 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_94'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_94 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_95'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_95 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_96'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_96 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_97'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_97 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_98'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_98 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_99'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_99 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_100'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_100 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_101'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_101 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_102'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_102 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_103'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_103 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_104'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_104 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_105'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_105 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_106'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_106 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_107'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_107 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_108'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_108 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_109'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_109 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_110'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_110 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_111'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_111 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_112'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_112 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_113'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_113 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_114'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_114 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_115'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_115 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_116'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_116 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_117'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_117 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_118'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_118 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_119'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_119 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_120'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_120 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_121'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_121 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_122'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_122 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_123'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_123 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_124'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_124 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_125'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_125 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_126'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_126 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_127'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_127 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_128'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_128 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_129'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_129 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_130'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_130 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_131'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_131 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_132'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_132 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_133'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_133 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_134'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_134 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_135'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_135 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_136'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_136 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_137'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_137 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_138'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_138 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_139'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_139 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_140'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_140 # type: ignore # mutmut generated
mutants_xǁCompilerDriverǁcompile_c_to_hack__mutmut['xǁCompilerDriverǁcompile_c_to_hack__mutmut_141'] = CompilerDriver.xǁCompilerDriverǁcompile_c_to_hack__mutmut_141 # type: ignore # mutmut generated
