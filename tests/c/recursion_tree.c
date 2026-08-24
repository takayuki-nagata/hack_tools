// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Deep Recursion, Mutual Recursion & Tree Traversal Test Program for Hack CPU

// 1. Ackermann function (deep recursive call tree)
__attribute__((noinline)) int ackermann(int m, int n) {
    if (m == 0) {
        return n + 1;
    } else if (m > 0 && n == 0) {
        return ackermann(m - 1, 1);
    } else {
        return ackermann(m - 1, ackermann(m, n - 1));
    }
}

// 2. Mutual recursion
int is_even(int n);

__attribute__((noinline)) int is_odd(int n) {
    if (n == 0)
        return 0;
    return is_even(n - 1);
}

__attribute__((noinline)) int is_even(int n) {
    if (n == 0)
        return 1;
    return is_odd(n - 1);
}

// 3. Binary Search Tree (BST)
typedef struct BSTNode {
    int key;
    int value;
    struct BSTNode *left;
    struct BSTNode *right;
} BSTNode;

__attribute__((noinline)) void bst_insert(BSTNode **root, BSTNode *new_node) {
    if (*root == 0) {
        *root = new_node;
        new_node->left = 0;
        new_node->right = 0;
        return;
    }
    if (new_node->key < (*root)->key) {
        bst_insert(&((*root)->left), new_node);
    } else {
        bst_insert(&((*root)->right), new_node);
    }
}

__attribute__((noinline)) int bst_sum_inorder(BSTNode *root) {
    if (root == 0)
        return 0;
    return bst_sum_inorder(root->left) + root->value + bst_sum_inorder(root->right);
}

__attribute__((noinline)) int bst_max_depth(BSTNode *root) {
    if (root == 0)
        return 0;
    int dl = bst_max_depth(root->left);
    int dr = bst_max_depth(root->right);
    return (dl > dr ? dl : dr) + 1;
}

int main(void) {
    // Ackermann tests:
    // A(2, 3) = 9
    // A(3, 2) = 29
    int a1 = ackermann(2, 3); // 9
    int a2 = ackermann(3, 2); // 29

    // Mutual recursion tests:
    int e1 = is_even(10); // 1
    int o1 = is_odd(10);  // 0
    int e2 = is_even(7);  // 0
    int o2 = is_odd(7);   // 1

    // BST tests:
    BSTNode nodes[6];
    BSTNode *root = 0;

    // Keys: 50, 20, 70, 10, 30, 80
    // Values: 5, 2, 7, 1, 3, 8
    nodes[0].key = 50;
    nodes[0].value = 5;
    nodes[1].key = 20;
    nodes[1].value = 2;
    nodes[2].key = 70;
    nodes[2].value = 7;
    nodes[3].key = 10;
    nodes[3].value = 1;
    nodes[4].key = 30;
    nodes[4].value = 3;
    nodes[5].key = 80;
    nodes[5].value = 8;

    for (int i = 0; i < 6; i++) {
        bst_insert(&root, &nodes[i]);
    }

    int bst_sum = bst_sum_inorder(root); // 1 + 2 + 3 + 5 + 7 + 8 = 26
    int bst_dep = bst_max_depth(root);   // 3

    // Total:
    // a1(9) + a2(29) = 38
    // e1(1) + o1(0) + e2(0) + o2(1) = 2
    // bst_sum(26) + bst_dep(3) = 29
    // Sum = 38 + 2 + 29 = 69
    return a1 + a2 + e1 + o1 + e2 + o2 + bst_sum + bst_dep;
}
