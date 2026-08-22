// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Max calculation test program for Hack CPU

int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int main(void) {
    return max(42, 17); // Expect 42
}
