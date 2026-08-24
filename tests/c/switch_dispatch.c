// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Switch Statement and Jump Table Test Program for Hack CPU

__attribute__((noinline)) int execute_opcode(int opcode, int operand_a, int operand_b) {
    int result = 0;
    switch (opcode) {
        case 0:
            result = operand_a + operand_b;
            break;
        case 1:
            result = operand_a - operand_b;
            break;
        case 2:
            result = operand_a * operand_b;
            break;
        case 3:
            result = (operand_b != 0) ? (operand_a / operand_b) : 0;
            break;
        case 4:
            result = operand_a & operand_b;
            break;
        case 5:
            result = operand_a | operand_b;
            break;
        case 6:
            result = operand_a ^ operand_b;
            break;
        case 100: // Sparse case
            result = (operand_a << 2) + operand_b;
            break;
        default:
            result = -1;
            break;
    }
    return result;
}

int main(void) {
    volatile int a = 12;
    volatile int b = 4;

    int r0 = execute_opcode(0, a, b);   // 16
    int r1 = execute_opcode(1, a, b);   // 8
    int r2 = execute_opcode(2, a, b);   // 48
    int r3 = execute_opcode(3, a, b);   // 3
    int r4 = execute_opcode(4, a, b);   // 4
    int r5 = execute_opcode(5, a, b);   // 12
    int r6 = execute_opcode(6, a, b);   // 8
    int r100 = execute_opcode(100, a, b); // 48 + 4 = 52
    int rdef = execute_opcode(999, a, b); // -1

    return r0 + r1 + r2 + r3 + r4 + r5 + r6 + r100 + rdef;
    // 16 + 8 + 48 + 3 + 4 + 12 + 8 + 52 - 1 = 150
}
