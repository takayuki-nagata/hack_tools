// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Memory-Mapped Screen Graphics Drawing Test Program for Hack CPU

#define SCREEN_BASE ((volatile int *)16384)
#define SCREEN_WIDTH_WORDS 32 // 512 pixels / 16 bits = 32 words per row

// Draw a horizontal line of full 16-bit blocks
__attribute__((noinline)) void draw_horizontal_bar(int start_row, int num_words, int pattern) {
    volatile int *screen = SCREEN_BASE + (start_row * SCREEN_WIDTH_WORDS);
    for (int col = 0; col < num_words; col++) {
        screen[col] = pattern;
    }
}

// Clear a rectangular region
__attribute__((noinline)) void clear_region(int start_row, int num_rows, int num_words) {
    for (int r = 0; r < num_rows; r++) {
        volatile int *row_ptr = SCREEN_BASE + ((start_row + r) * SCREEN_WIDTH_WORDS);
        for (int c = 0; c < num_words; c++) {
            row_ptr[c] = 0;
        }
    }
}

// Set a single pixel bit
__attribute__((noinline)) void set_pixel(int x, int y) {
    int word_idx = (y * SCREEN_WIDTH_WORDS) + (x / 16);
    int bit_pos = x % 16;
    int mask = 1 << bit_pos;
    SCREEN_BASE[word_idx] |= mask;
}

int main(void) {
    // 1. Draw a test bar with pattern 0x5555 (0b0101010101010101)
    draw_horizontal_bar(10, 4, 0x5555);

    // 2. Set individual pixels
    set_pixel(0, 0);
    set_pixel(15, 0);
    set_pixel(16, 0);

    // 3. Read back from memory-mapped screen to verify written values
    int val_bar = SCREEN_BASE[10 * SCREEN_WIDTH_WORDS]; // 0x5555 (21845)
    int val_pix0 = SCREEN_BASE[0];                      // (1 << 0) | (1 << 15) = 1 | (-32768)
    int val_pix1 = SCREEN_BASE[1];                      // (1 << 0) = 1

    clear_region(10, 1, 4);
    int val_cleared = SCREEN_BASE[10 * SCREEN_WIDTH_WORDS]; // 0

    return (val_bar != 0) + (val_pix0 != 0) + (val_pix1 == 1) +
           (val_cleared == 0); // 1 + 1 + 1 + 1 = 4
}
