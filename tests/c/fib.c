// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Fibonacci recursive test program for Hack CPU

int fib(int n) {
    if (n <= 0)
        return 0;
    if (n == 1)
        return 1;
    return fib(n - 1) + fib(n - 2);
}

int main(void) {
    return fib(7); // Expect 13
}
