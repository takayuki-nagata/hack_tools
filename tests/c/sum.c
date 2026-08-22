// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Sum calculation test program for Hack CPU

int sum(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) {
        s += i;
    }
    return s;
}

int main(void) {
    return sum(10); // Expect 55
}
