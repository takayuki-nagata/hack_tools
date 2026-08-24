// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Math calculation test program (multiplication, division, modulo, noinline calls)

__attribute__((noinline)) int multiply(int a, int b) {
    return a * b;
}

__attribute__((noinline)) int divide(int a, int b) {
    return a / b;
}

__attribute__((noinline)) int modulo(int a, int b) {
    return a % b;
}

// Function using multiple callee-saved registers to trigger __mspabi_func_epilog_N
__attribute__((noinline)) int complex_calc(int x, int y, int z, int w) {
    int a = x * 2;
    int b = y * 3;
    int c = z / 2;
    int d = w % 5;
    return a + b + c + d;
}

int main(void) {
    volatile int x = 6;
    volatile int y = 7;
    volatile int a = 100;
    volatile int b = 7;

    int prod = multiply(x, y);          // 42
    int quot = divide(a, b);            // 14
    int rem = modulo(a, b);             // 2
    int comp = complex_calc(x, y, a, b);// 12 + 21 + 50 + 2 = 85

    return prod + quot + rem + comp;    // 58 + 85 = 143
}
