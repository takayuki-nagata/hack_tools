// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// QuickSort & Binary Search In-Place Algorithm Test Program for Hack CPU

__attribute__((noinline)) void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

__attribute__((noinline)) int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

__attribute__((noinline)) void quicksort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

__attribute__((noinline)) int binary_search(const int arr[], int len, int target) {
    int low = 0;
    int high = len - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

int main(void) {
    // Array with negatives, duplicates, unsorted:
    // [45, -12, 88, 0, -12, 33, 7, 100, -50, 12]
    int arr[10];
    arr[0] = 45;
    arr[1] = -12;
    arr[2] = 88;
    arr[3] = 0;
    arr[4] = -12;
    arr[5] = 33;
    arr[6] = 7;
    arr[7] = 100;
    arr[8] = -50;
    arr[9] = 12;

    quicksort(arr, 0, 9);

    // Expected sorted:
    // [-50, -12, -12, 0, 7, 12, 33, 45, 88, 100]
    // Check sorted array ordering:
    int is_sorted = 1;
    for (int i = 0; i < 9; i++) {
        if (arr[i] > arr[i + 1]) {
            is_sorted = 0;
        }
    }

    // Binary search queries:
    int idx_neg50 = binary_search(arr, 10, -50); // 0
    int idx_0 = binary_search(arr, 10, 0);       // 3
    int idx_33 = binary_search(arr, 10, 33);     // 6
    int idx_100 = binary_search(arr, 10, 100);   // 9
    int idx_miss = binary_search(arr, 10, 999);  // -1

    // Weighted checksum of sorted array:
    // sum(arr[i] * (i + 1))
    // -50*1 + -12*2 + -12*3 + 0*4 + 7*5 + 12*6 + 33*7 + 45*8 + 88*9 + 100*10
    // = -50 - 24 - 36 + 0 + 35 + 72 + 231 + 360 + 792 + 1000
    // = 2380
    int weighted_sum = 0;
    for (int i = 0; i < 10; i++) {
        weighted_sum += arr[i] * (i + 1);
    }

    // Return total:
    // is_sorted(1) + idx_neg50(0) + idx_0(3) + idx_33(6) + idx_100(9) + idx_miss(-1) +
    // weighted_sum(2380) = 1 + 0 + 3 + 6 + 9 - 1 + 2380 = 2398
    return is_sorted + idx_neg50 + idx_0 + idx_33 + idx_100 + idx_miss + weighted_sum;
}
