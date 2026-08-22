#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
HAS_BIN="${HAS_BIN:-${REPO_ROOT}/has/has}"
OUT_DIR="${REPO_ROOT}/test_out"

mkdir -p "${OUT_DIR}"

PASSED=0
FAILED=0

run_test() {
    local test_name="$1"
    shift
    echo -n "Running [${test_name}]... "
    if "$@"; then
        echo "PASSED"
        PASSED=$((PASSED + 1))
    else
        echo "FAILED"
        FAILED=$((FAILED + 1))
    fi
}

assert_file_equal() {
    local file1="$1"
    local file2="$2"
    if ! cmp -s "${file1}" "${file2}"; then
        echo "Files ${file1} and ${file2} differ:"
        diff -u "${file1}" "${file2}" || true
        return 1
    fi
    return 0
}

# 1. Normal Hack Output Tests
test_hack_asm() {
    local asm_name="$1"
    local asm_file="${SCRIPT_DIR}/asm/${asm_name}.asm"
    local exp_file="${SCRIPT_DIR}/expected/${asm_name}.hack"
    local out_file="${OUT_DIR}/${asm_name}.hack"

    "${HAS_BIN}" -o "${out_file}" "${asm_file}"
    assert_file_equal "${exp_file}" "${out_file}"
}

# 2. Output to stdout
test_stdout() {
    local asm_file="${SCRIPT_DIR}/asm/math_loop.asm"
    local exp_file="${SCRIPT_DIR}/expected/math_loop.hack"
    local out_file="${OUT_DIR}/stdout_math_loop.hack"

    "${HAS_BIN}" -s "${asm_file}" > "${out_file}"
    assert_file_equal "${exp_file}" "${out_file}"
}

# 3. Default Outfile Generation (same directory as input)
test_default_outfile() {
    local tmp_asm="${OUT_DIR}/default_test.asm"
    local exp_file="${SCRIPT_DIR}/expected/edge_cases.hack"
    cp "${SCRIPT_DIR}/asm/edge_cases.asm" "${tmp_asm}"

    "${HAS_BIN}" "${tmp_asm}"
    assert_file_equal "${exp_file}" "${OUT_DIR}/default_test.hack"
}

# 4. Raw Binary Output Format
test_raw_binary() {
    local asm_file="${SCRIPT_DIR}/asm/math_loop.asm"
    local bin_file="${OUT_DIR}/math_loop.bin"

    "${HAS_BIN}" -r -o "${bin_file}" "${asm_file}"
    
    # 20 instructions * 2 bytes = 40 bytes
    local file_sz
    file_sz=$(wc -c < "${bin_file}")
    if [ "${file_sz}" -ne 40 ]; then
        echo "Unexpected file size ${file_sz}, expected 40"
        return 1
    fi

    # Check first instruction @2 (0x0002) in big-endian
    local first_bytes
    first_bytes=$(hexdump -n 2 -e '2/1 "%02x "' "${bin_file}" | tr -d ' ')
    if [ "${first_bytes}" != "0002" ]; then
        echo "Unexpected first bytes: ${first_bytes}, expected 0002"
        return 1
    fi
    return 0
}

# 5. COE Format Output
test_coe_format() {
    local asm_file="${SCRIPT_DIR}/asm/math_loop.asm"
    local coe_file="${OUT_DIR}/math_loop.coe"

    "${HAS_BIN}" -c -o "${coe_file}" "${asm_file}"
    
    # Header check
    if ! grep -q "memory_initialization_radix=16;" "${coe_file}"; then
        echo "COE header missing radix"
        return 1
    fi
    if ! grep -q "memory_initialization_vector=" "${coe_file}"; then
        echo "COE header missing vector"
        return 1
    fi
    # Footer check
    if ! tail -n 1 "${coe_file}" | grep -q ";"; then
        echo "COE footer missing semicolon"
        return 1
    fi
    return 0
}

# 6. CLI Flags
test_cli_flags() {
    # Help flags
    "${HAS_BIN}" -h > /dev/null
    "${HAS_BIN}" --help > /dev/null

    # Version flags
    "${HAS_BIN}" -v > /dev/null
    "${HAS_BIN}" --version > /dev/null

    # Long option stdout
    "${HAS_BIN}" --stdout "${SCRIPT_DIR}/asm/edge_cases.asm" > /dev/null

    # Long option raw / coe
    "${HAS_BIN}" --raw -o "${OUT_DIR}/flag_test.bin" "${SCRIPT_DIR}/asm/edge_cases.asm"
    "${HAS_BIN}" --coe -o "${OUT_DIR}/flag_test.coe" "${SCRIPT_DIR}/asm/edge_cases.asm"
    return 0
}

# 7. Error Handling Tests
test_error_handling() {
    local bad_asm_dir="${OUT_DIR}/bad_asm"
    mkdir -p "${bad_asm_dir}"

    # Missing arguments
    if "${HAS_BIN}" 2>/dev/null; then return 1; fi

    # Invalid option
    if "${HAS_BIN}" -z 2>/dev/null; then return 1; fi

    # Invalid extension
    if "${HAS_BIN}" "${OUT_DIR}/test.txt" 2>/dev/null; then return 1; fi

    # No extension
    if "${HAS_BIN}" "${OUT_DIR}/no_extension" 2>/dev/null; then return 1; fi

    # Nonexistent file
    if "${HAS_BIN}" "${OUT_DIR}/nonexistent.asm" 2>/dev/null; then return 1; fi

    # Bad comp
    echo "D=UNKNOWN" > "${bad_asm_dir}/bad_comp.asm"
    if "${HAS_BIN}" "${bad_asm_dir}/bad_comp.asm" 2>/dev/null; then return 1; fi

    # Bad dest
    echo "INVALID=D" > "${bad_asm_dir}/bad_dest.asm"
    if "${HAS_BIN}" "${bad_asm_dir}/bad_dest.asm" 2>/dev/null; then return 1; fi

    # Bad jump
    echo "0;JINVALID" > "${bad_asm_dir}/bad_jump.asm"
    if "${HAS_BIN}" "${bad_asm_dir}/bad_jump.asm" 2>/dev/null; then return 1; fi

    # Unclosed label
    echo "(UNCLOSED_LABEL" > "${bad_asm_dir}/unclosed_label.asm"
    if "${HAS_BIN}" "${bad_asm_dir}/unclosed_label.asm" 2>/dev/null; then return 1; fi

    # Empty label
    echo "()" > "${bad_asm_dir}/empty_label.asm"
    if "${HAS_BIN}" "${bad_asm_dir}/empty_label.asm" 2>/dev/null; then return 1; fi

    # Empty A-instruction
    echo "@" > "${bad_asm_dir}/empty_a.asm"
    if "${HAS_BIN}" "${bad_asm_dir}/empty_a.asm" 2>/dev/null; then return 1; fi

    # Out of range constant
    echo "@32768" > "${bad_asm_dir}/range.asm"
    if "${HAS_BIN}" "${bad_asm_dir}/range.asm" 2>/dev/null; then return 1; fi

    # Negative constant
    echo "@-1" > "${bad_asm_dir}/negative.asm"
    if "${HAS_BIN}" "${bad_asm_dir}/negative.asm" 2>/dev/null; then return 1; fi

    # Unwritable output file
    if "${HAS_BIN}" -o "/proc/non_writable_file" "${SCRIPT_DIR}/asm/edge_cases.asm" 2>/dev/null; then return 1; fi

    # Unwritable directory with default outfile (triggers allocated_outfile free on open error)
    local ro_dir="${bad_asm_dir}/readonly_dir"
    mkdir -p "${ro_dir}"
    cp "${SCRIPT_DIR}/asm/edge_cases.asm" "${ro_dir}/test.asm"
    chmod 555 "${ro_dir}"
    if "${HAS_BIN}" "${ro_dir}/test.asm" 2>/dev/null; then
        chmod 755 "${ro_dir}"
        return 1
    fi
    chmod 755 "${ro_dir}"

    return 0
}

# 8. C Unit Tests
test_c_unit() {
    if [ -x "${REPO_ROOT}/tests/unit_test" ]; then
        "${REPO_ROOT}/tests/unit_test" > /dev/null
    fi
}

echo "=== Running hack_tools (has) Test Suite ==="
run_test "C unit tests"         test_c_unit
run_test "all_instructions.asm" test_hack_asm "all_instructions"
run_test "symbols.asm"          test_hack_asm "symbols"
run_test "math_loop.asm"        test_hack_asm "math_loop"
run_test "edge_cases.asm"       test_hack_asm "edge_cases"
run_test "stdout mode (-s)"     test_stdout
run_test "default outfile"      test_default_outfile
run_test "raw binary format"    test_raw_binary
run_test "COE format"           test_coe_format
run_test "CLI flags"            test_cli_flags
run_test "error handling"       test_error_handling

echo ""
echo "=== Test Results: ${PASSED} passed, ${FAILED} failed ==="
if [ "${FAILED}" -gt 0 ]; then
    exit 1
fi
