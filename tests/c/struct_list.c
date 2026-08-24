// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Linked List and Struct Operations Test Program for Hack CPU

typedef struct Node {
    int value;
    int key;
    struct Node *next;
} Node;

typedef struct List {
    Node *head;
    int size;
} List;

__attribute__((noinline)) void list_init(List *list) {
    list->head = 0;
    list->size = 0;
}

__attribute__((noinline)) void list_push_front(List *list, Node *node, int key, int value) {
    node->key = key;
    node->value = value;
    node->next = list->head;
    list->head = node;
    list->size++;
}

__attribute__((noinline)) int list_sum_values(const List *list) {
    int sum = 0;
    Node *curr = list->head;
    while (curr != 0) {
        sum += curr->value;
        curr = curr->next;
    }
    return sum;
}

__attribute__((noinline)) void list_reverse(List *list) {
    Node *prev = 0;
    Node *curr = list->head;
    Node *next = 0;

    while (curr != 0) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    list->head = prev;
}

int main(void) {
    List list;
    Node nodes[4];

    list_init(&list);
    list_push_front(&list, &nodes[0], 1, 10);
    list_push_front(&list, &nodes[1], 2, 20);
    list_push_front(&list, &nodes[2], 3, 30);
    list_push_front(&list, &nodes[3], 4, 40);

    int sum_before = list_sum_values(&list); // 100
    list_reverse(&list);
    int head_val = list.head ? list.head->value : 0; // 10

    return sum_before + head_val + list.size; // 100 + 10 + 4 = 114
}
