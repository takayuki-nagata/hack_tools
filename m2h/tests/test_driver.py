# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

import os
import tempfile
from unittest.mock import patch

import pytest

from m2h.driver import CompilerDriver, find_executable, get_compiler_version_info, run_command
from m2h.hcc import main as hcc_main
from m2h.hcc import normalize_opt_level


def test_normalize_opt_level() -> None:
    assert normalize_opt_level("2") == "-O2"
    assert normalize_opt_level("-O2") == "-O2"
    assert normalize_opt_level("O3") == "-O3"
    assert normalize_opt_level("s") == "-Os"


def test_find_executable() -> None:
    # Existing in path (e.g. sh, python3)
    assert find_executable("python3") is not None
    # Nonexistent
    assert find_executable("nonexistent_binary_12345") is None
    # Fallback path
    with tempfile.NamedTemporaryFile() as tf:
        os.chmod(tf.name, 0o755)
        found = find_executable("custom_tool", fallback_paths=[tf.name])
        assert found == tf.name


def test_get_compiler_version_info() -> None:
    # Mock successful version output (9.3.1)
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "msp430-elf-gcc (Mitto Systems Limited) 9.3.1.11\n"
        mock_run.return_value.stderr = ""
        info = get_compiler_version_info("msp430-elf-gcc")
        assert info is not None
        major, minor, patch_v, first_line = info
        assert major == 9
        assert minor == 3
        assert patch_v == 1
        assert "9.3.1.11" in first_line

    # Mock old version output (4.6.3)
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "msp430-gcc (GCC) 4.6.3 20120306\n"
        mock_run.return_value.stderr = ""
        info = get_compiler_version_info("msp430-gcc")
        assert info is not None
        assert info[0] == 4

    # Mock empty / non-matching output
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = ""
        mock_run.return_value.stderr = ""
        assert get_compiler_version_info("empty-cc") is None

    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "Unknown compiler\n"
        mock_run.return_value.stderr = ""
        assert get_compiler_version_info("unknown-cc") is None

    # Mock exception
    with patch("subprocess.run", side_effect=OSError("fail")):
        assert get_compiler_version_info("bad-cc") is None


def test_run_command() -> None:
    # Successful command
    assert run_command(["echo", "hello"]) == 0
    # Failing command with stdout only
    assert run_command(["python3", "-c", "import sys; sys.stdout.write('fail'); sys.exit(1)"]) == 1
    # Failing command with stderr
    assert run_command(["ls", "/nonexistent_path_12345"]) != 0
    # Command raising exception
    assert run_command(["/invalid/path/to/binary/cannot/run"]) != 0


def test_driver_compile_errors(capsys: pytest.CaptureFixture[str]) -> None:
    driver = CompilerDriver(cc="msp430-gcc", has="has")

    # Nonexistent input file
    ret = driver.compile_c_to_hack("nonexistent.c")
    assert ret == 1
    assert "not found" in capsys.readouterr().err

    # Compiler not in PATH
    with tempfile.NamedTemporaryFile(suffix=".c") as tf:
        bad_driver = CompilerDriver(cc="nonexistent_gcc_12345")
        ret = bad_driver.compile_c_to_hack(tf.name)
        assert ret == 1
        assert "not found in PATH" in capsys.readouterr().err


def test_driver_compiler_version_warning(capsys: pytest.CaptureFixture[str]) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        input_c = os.path.join(tmpdir, "main.c")
        with open(input_c, "w", encoding="utf-8") as f:
            f.write("int main(void) { return 0; }\n")

        with (
            patch("shutil.which", return_value="/usr/bin/msp430-gcc"),
            patch(
                "m2h.driver.get_compiler_version_info",
                return_value=(4, 6, 3, "msp430-gcc 4.6.3"),
            ),
            patch("m2h.driver.run_command", return_value=0),
            patch("m2h.driver.transpile_file", return_value=0),
        ):
            driver = CompilerDriver(cc="msp430-gcc", has="has")
            ret = driver.compile_c_to_hack(input_c, output_path=os.path.join(tmpdir, "out.hack"))
            assert ret == 0
            err_output = capsys.readouterr().err
            assert "warning: MSP430 GCC version '4.6.3' detected" in err_output


def test_driver_compile_pipeline_mocked() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        input_c = os.path.join(tmpdir, "main.c")
        with open(input_c, "w", encoding="utf-8") as f:
            f.write("int main(void) { return 0; }\n")

        out_hack = os.path.join(tmpdir, "main.hack")
        out_asm = os.path.join(tmpdir, "main.asm")

        def fake_transpile(input_path: str, output_path: str = "", **kwargs: object) -> int:
            if output_path:
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write("@0\nD=A\n")
            return 0

        # Mock compiler and assembler calls
        with (
            patch("shutil.which", return_value="/usr/bin/mock"),
            patch("m2h.driver.run_command", return_value=0),
            patch("m2h.driver.transpile_file", side_effect=fake_transpile),
        ):
            driver = CompilerDriver(cc="msp430-gcc", has="has")

            # Standard compile
            ret = driver.compile_c_to_hack(input_c, output_path=out_hack)
            assert ret == 0

            # Standard compile with raw and coe formats
            ret = driver.compile_c_to_hack(input_c, output_path=out_hack, format_type="raw")
            assert ret == 0

            ret = driver.compile_c_to_hack(input_c, output_path=out_hack, format_type="coe")
            assert ret == 0

            ret = driver.compile_c_to_hack(input_c, stdout_mode=True)
            assert ret == 0

            # Keep temps
            ret = driver.compile_c_to_hack(input_c, keep_temps=True)
            assert ret == 0

            # Stop at assembly (-S)
            ret = driver.compile_c_to_hack(input_c, output_path=out_asm, stop_at_asm=True)
            assert ret == 0

            # Stop at assembly to stdout
            ret = driver.compile_c_to_hack(input_c, stop_at_asm=True, stdout_mode=True)
            assert ret == 0

            # Assembler not found
            driver_no_has = CompilerDriver(cc="msp430-gcc", has="nonexistent_has_12345")
            with (
                patch("shutil.which", side_effect=lambda x: "/bin/gcc" if "gcc" in x else None),
                patch("os.path.isfile", return_value=False),
            ):
                ret = driver_no_has.compile_c_to_hack(input_c, output_path=out_hack)
                assert ret == 1

            # GCC failure
            with patch("m2h.driver.run_command", return_value=1):
                ret = driver.compile_c_to_hack(input_c, output_path=out_hack)
                assert ret == 1

            # m2h failure
            with (
                patch("m2h.driver.run_command", return_value=0),
                patch("m2h.driver.transpile_file", return_value=1),
            ):
                ret = driver.compile_c_to_hack(input_c, output_path=out_hack)
                assert ret == 1

            # has failure
            with (
                patch("m2h.driver.run_command", side_effect=[0, 1]),
                patch("m2h.driver.transpile_file", side_effect=fake_transpile),
            ):
                ret = driver.compile_c_to_hack(input_c, output_path=out_hack)
                assert ret == 1


def test_hcc_cli() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        input_c = os.path.join(tmpdir, "main.c")
        with open(input_c, "w", encoding="utf-8") as f:
            f.write("int main(void) { return 0; }\n")

        with patch("m2h.driver.CompilerDriver.compile_c_to_hack", return_value=0) as mock_compile:
            # Standard
            ret = hcc_main([input_c, "-o", "out.hack", "-O3", "-k"])
            assert ret == 0
            mock_compile.assert_called_with(
                input_c_path=input_c,
                output_path="out.hack",
                format_type="hack",
                stdout_mode=False,
                stop_at_asm=False,
                keep_temps=True,
                opt_level="-O3",
                include_crt0=True,
            )

            # Raw binary & no-crt0
            ret = hcc_main([input_c, "-r", "--no-crt0"])
            assert ret == 0

            # COE format & assemble-only
            ret = hcc_main([input_c, "-c", "-S", "-s"])
            assert ret == 0

    # Help & Version
    with pytest.raises(SystemExit) as exc:
        hcc_main(["-h"])
    assert exc.value.code == 0

    with pytest.raises(SystemExit) as exc:
        hcc_main(["-v"])
    assert exc.value.code == 0
