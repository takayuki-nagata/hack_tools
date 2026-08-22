// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Array and pointer manipulation test program for Hack CPU

int sum_array(const int *arr, int len) {
    int total = 0;
    for (int i = 0; i < len; i++) {
        total += arr[i];
    }
    return total;
}

int main(void) {
    int data[4];
    data[0] = 10;
    data[1] = 20;
    data[2] = 30;
    data[3] = 40;
    return sum_array(data, 4); // Expect 100
}
