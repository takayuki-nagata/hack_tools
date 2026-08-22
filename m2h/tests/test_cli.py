# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

import os
import tempfile

import pytest

from m2h.cli import derive_outfile_name, main, transpile_file


def test_derive_outfile_name() -> None:
    assert derive_outfile_name("foo.s") == "foo.asm"
    assert derive_outfile_name("path/to/test.s") == "path/to/test.asm"


def test_transpile_file_success() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        input_s = os.path.join(tmpdir, "test.s")
        output_asm = os.path.join(tmpdir, "test.asm")

        with open(input_s, "w", encoding="utf-8") as f:
            f.write("main:\n  mov #10, r12\n  ret\n")

        # Transpile to file
        ret = transpile_file(input_s, output_asm, to_stdout=False, include_crt0=True)
        assert ret == 0
        assert os.path.exists(output_asm)
        with open(output_asm, encoding="utf-8") as f:
            content = f.read()
            assert "@10" in content
            assert "@SP" in content

        # Default outfile name
        ret = transpile_file(input_s, None, to_stdout=False, include_crt0=False)
        assert ret == 0
        assert os.path.exists(os.path.join(tmpdir, "test.asm"))


def test_transpile_file_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        input_s = os.path.join(tmpdir, "test.s")
        with open(input_s, "w", encoding="utf-8") as f:
            f.write("main:\n  mov #42, r12\n  ret\n")

        ret = transpile_file(input_s, to_stdout=True, include_crt0=False)
        assert ret == 0
        captured = capsys.readouterr()
        assert "@42" in captured.out


def test_transpile_file_errors(capsys: pytest.CaptureFixture[str]) -> None:
    # Nonexistent file
    ret = transpile_file("nonexistent_file.s")
    assert ret == 1
    assert "not found" in capsys.readouterr().err

    # Invalid syntax in asm
    with tempfile.TemporaryDirectory() as tmpdir:
        bad_s = os.path.join(tmpdir, "bad.s")
        with open(bad_s, "w", encoding="utf-8") as f:
            f.write("bad_instruction_here 123\n")

        ret = transpile_file(bad_s)
        assert ret == 1
        assert "error during transpilation" in capsys.readouterr().err

        # Unwritable output file
        valid_s = os.path.join(tmpdir, "valid.s")
        with open(valid_s, "w", encoding="utf-8") as f:
            f.write("main:\n  ret\n")

        ret = transpile_file(valid_s, output_path="/proc/non_writable_file")
        assert ret == 1
        assert "error writing" in capsys.readouterr().err


def test_main_cli(capsys: pytest.CaptureFixture[str]) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        input_s = os.path.join(tmpdir, "test.s")
        with open(input_s, "w", encoding="utf-8") as f:
            f.write("main:\n  ret\n")

        out_asm = os.path.join(tmpdir, "out.asm")
        ret = main([input_s, "-o", out_asm, "--no-crt0"])
        assert ret == 0
        assert os.path.exists(out_asm)

        # Help
        with pytest.raises(SystemExit) as exc:
            main(["-h"])
        assert exc.value.code == 0

        # Version
        with pytest.raises(SystemExit) as exc:
            main(["-v"])
        assert exc.value.code == 0
