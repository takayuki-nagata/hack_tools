// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Bit Manipulation & Extreme Arithmetic Boundary Test Program for Hack CPU

__attribute__((noinline)) int popcount(int val) {
    int count = 0;
    unsigned int v = (unsigned int)val;
    while (v != 0) {
        if (v & 1) {
            count++;
        }
        v >>= 1;
    }
    return count;
}

__attribute__((noinline)) int bswap16(int val) {
    return ((val & 0x00FF) << 8) | ((val >> 8) & 0x00FF);
}

__attribute__((noinline)) int is_power_of_two(int val) {
    if (val <= 0) return 0;
    return (val & (val - 1)) == 0;
}

__attribute__((noinline)) int sign_extend_byte(int byte_val) {
    int b = byte_val & 0xFF;
    if (b & 0x80) {
        return b | (~0xFF);
    }
    return b;
}

__attribute__((noinline)) int signed_math_boundaries(void) {
    volatile int neg_a = -30;
    volatile int pos_b = 7;
    volatile int neg_b = -7;

    int q1 = neg_a / pos_b; // -4
    int r1 = neg_a % pos_b; // -2
    int q2 = 30 / neg_b;    // -4
    int r2 = 30 % neg_b;    // 2
    int q3 = neg_a / neg_b; // 4
    int r3 = neg_a % neg_b; // -2

    return q1 + r1 + q2 + r2 + q3 + r3; // -4 - 2 - 4 + 2 + 4 - 2 = -6
}

int main(void) {
    // 1. Popcount tests:
    // 0x5555 (0b0101010101010101) has 8 bits
    // 0xFFFF (-1) has 16 bits
    // 0x0000 has 0 bits
    int p1 = popcount(0x5555); // 8
    int p2 = popcount(-1);     // 16
    int p3 = popcount(0);      // 0

    // 2. Byte swap tests:
    // 0x1234 -> 0x3412 (13330)
    int s1 = bswap16(0x1234); // 0x3412 = 13330

    // 3. Power of two tests:
    int pow1 = is_power_of_two(1024); // 1
    int pow2 = is_power_of_two(1023); // 0
    int pow3 = is_power_of_two(1);    // 1
    int pow4 = is_power_of_two(0);    // 0
    int pow5 = is_power_of_two(-16);  // 0

    // 4. Sign extension tests:
    int ext1 = sign_extend_byte(0x7F); // +127
    int ext2 = sign_extend_byte(0x80); // -128
    int ext3 = sign_extend_byte(0xFF); // -1

    // 5. Signed math boundary tests:
    int smath = signed_math_boundaries(); // -6

    // Total verification score:
    // p1(8) + p2(16) + p3(0) = 24
    // s1(13330)
    // pow(1+0+1+0+0) = 2
    // ext(127 + (-128) + (-1)) = -2
    // smath(-6)
    // Total = 24 + 13330 + 2 - 2 - 6 = 13348
    return p1 + p2 + p3 + s1 + pow1 + pow2 + pow3 + pow4 + pow5 + ext1 + ext2 + ext3 + smath;
}
