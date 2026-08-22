# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

import os
import runpy
import tempfile
from unittest.mock import patch

import pytest

from m2h.cli import transpile_file
from m2h.driver import CompilerDriver
from m2h.emitter import HackEmitter
from m2h.parser import Operand, OperandType


def test_main_modules_execution() -> None:
    # Test __main__.py execution
    with patch("sys.argv", ["m2h", "-h"]), pytest.raises(SystemExit) as exc:
        runpy.run_module("m2h", run_name="__main__")
    assert exc.value.code == 0

    # Test cli.py as __main__
    with patch("sys.argv", ["m2h", "-h"]), pytest.raises(SystemExit) as exc:
        runpy.run_module("m2h.cli", run_name="__main__")
    assert exc.value.code == 0

    # Test hcc.py as __main__
    with patch("sys.argv", ["hcc", "-h"]), pytest.raises(SystemExit) as exc:
        runpy.run_module("m2h.hcc", run_name="__main__")
    assert exc.value.code == 0


def test_cli_read_exception(capsys: pytest.CaptureFixture[str]) -> None:
    with (
        tempfile.NamedTemporaryFile() as tf,
        patch("builtins.open", side_effect=PermissionError("Permission denied")),
    ):
        ret = transpile_file(tf.name)
        assert ret == 1
        assert "error reading" in capsys.readouterr().err


def test_driver_stop_at_asm_custom_output() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        input_c = os.path.join(tmpdir, "main.c")
        with open(input_c, "w", encoding="utf-8") as f:
            f.write("int main(void) { return 0; }\n")

        custom_asm = os.path.join(tmpdir, "custom.asm")

        def fake_transpile(input_path: str, output_path: str = "", **kwargs: object) -> int:
            if output_path:
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write("@0\nD=A\n")
            return 0

        with (
            patch("shutil.which", return_value="/usr/bin/mock"),
            patch("m2h.driver.run_command", return_value=0),
            patch("m2h.driver.transpile_file", side_effect=fake_transpile),
        ):
            driver = CompilerDriver(cc="msp430-gcc", has="has")
            ret = driver.compile_c_to_hack(input_c, stop_at_asm=True, output_path=custom_asm)
            assert ret == 0
            assert os.path.exists(custom_asm)


def test_emitter_invalid_operand_type() -> None:
    emitter = HackEmitter()
    invalid_op = Operand(op_type=cast_invalid_type(), value="test")
    with pytest.raises(ValueError, match="Unsupported operand type"):
        emitter.emit_load_operand(invalid_op)


def test_operand_str_fallback() -> None:
    op = Operand(op_type=cast_invalid_type(), value="fallback_value")
    assert str(op) == "fallback_value"


def cast_invalid_type() -> OperandType:
    return "UNKNOWN_TYPE"  # type: ignore[return-value]
