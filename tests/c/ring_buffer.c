// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Circular Queue / Ring Buffer Test Program for Embedded Hack CPU

#define QUEUE_CAPACITY 8

typedef struct RingBuffer {
    int buffer[QUEUE_CAPACITY];
    int head;
    int tail;
    int count;
} RingBuffer;

__attribute__((noinline)) void rb_init(RingBuffer *rb) {
    rb->head = 0;
    rb->tail = 0;
    rb->count = 0;
    for (int i = 0; i < QUEUE_CAPACITY; i++) {
        rb->buffer[i] = 0;
    }
}

__attribute__((noinline)) int rb_enqueue(RingBuffer *rb, int val) {
    if (rb->count >= QUEUE_CAPACITY) {
        return 0; // Full
    }
    rb->buffer[rb->tail] = val;
    rb->tail = (rb->tail + 1) % QUEUE_CAPACITY;
    rb->count++;
    return 1;
}

__attribute__((noinline)) int rb_dequeue(RingBuffer *rb, int *out_val) {
    if (rb->count <= 0) {
        return 0; // Empty
    }
    *out_val = rb->buffer[rb->head];
    rb->head = (rb->head + 1) % QUEUE_CAPACITY;
    rb->count--;
    return 1;
}

int main(void) {
    RingBuffer rb;
    rb_init(&rb);

    // Enqueue 5 items
    for (int i = 1; i <= 5; i++) {
        rb_enqueue(&rb, i * 10);
    }

    // Dequeue 2 items (10, 20)
    int v1 = 0, v2 = 0;
    rb_dequeue(&rb, &v1);
    rb_dequeue(&rb, &v2);

    // Enqueue 3 more items (60, 70, 80) -> tests ring buffer wrap-around
    rb_enqueue(&rb, 60);
    rb_enqueue(&rb, 70);
    rb_enqueue(&rb, 80);

    int sum_remaining = 0;
    int item = 0;
    while (rb_dequeue(&rb, &item)) {
        sum_remaining += item; // 30 + 40 + 50 + 60 + 70 + 80 = 330
    }

    return v1 + v2 + sum_remaining + rb.count; // 10 + 20 + 330 + 0 = 360
}
