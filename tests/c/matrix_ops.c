// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// 2D Matrix Operations, Determinant & Linear Algebra Test Program for Hack CPU

#define N 3

__attribute__((noinline)) void mat_mult(const int a[N][N], const int b[N][N], int c[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int sum = 0;
            for (int k = 0; k < N; k++) {
                sum += a[i][k] * b[k][j];
            }
            c[i][j] = sum;
        }
    }
}

__attribute__((noinline)) int mat_trace(const int a[N][N]) {
    int tr = 0;
    for (int i = 0; i < N; i++) {
        tr += a[i][i];
    }
    return tr;
}

__attribute__((noinline)) int mat_det3x3(const int m[N][N]) {
    int a = m[0][0], b = m[0][1], c = m[0][2];
    int d = m[1][0], e = m[1][1], f = m[1][2];
    int g = m[2][0], h = m[2][1], k = m[2][2];

    int det = a * (e * k - f * h) - b * (d * k - f * g) + c * (d * h - e * g);
    return det;
}

__attribute__((noinline)) void mat_transpose(const int src[N][N], int dst[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            dst[j][i] = src[i][j];
        }
    }
}

int main(void) {
    int a[N][N];
    a[0][0] = 1; a[0][1] = 2; a[0][2] = 3;
    a[1][0] = 0; a[1][1] = 1; a[1][2] = 4;
    a[2][0] = 5; a[2][1] = 6; a[2][2] = 0;

    int b[N][N];
    b[0][0] = 2; b[0][1] = 0; b[0][2] = -1;
    b[1][0] = 1; b[1][1] = 3; b[1][2] = 2;
    b[2][0] = 0; b[2][1] = -2; b[2][2] = 1;

    int c[N][N];
    mat_mult(a, b, c);

    // C = A * B:
    // row 0: [1*2 + 2*1 + 3*0, 1*0 + 2*3 + 3*(-2), 1*(-1) + 2*2 + 3*1] = [4, 0, 6]
    // row 1: [0*2 + 1*1 + 4*0, 0*0 + 1*3 + 4*(-2), 0*(-1) + 1*2 + 4*1] = [1, -5, 6]
    // row 2: [5*2 + 6*1 + 0*0, 5*0 + 6*3 + 0*(-2), 5*(-1) + 6*2 + 0*1] = [16, 18, 7]
    // Trace(C) = 4 + (-5) + 7 = 6
    int trace_c = mat_trace(c); // 6

    // det(A) = 1*(0 - 24) - 2*(0 - 20) + 3*(0 - 5) = -24 + 40 - 15 = 1
    int det_a = mat_det3x3(a); // 1

    // det(B) = 2*(3 - (-4)) - 0 + (-1)*(-2 - 0) = 2*(7) + 2 = 16
    int det_b = mat_det3x3(b); // 16

    // det(C) = det(A) * det(B) = 1 * 16 = 16
    int det_c = mat_det3x3(c); // 16

    int c_t[N][N];
    mat_transpose(c, c_t);
    int trace_ct = mat_trace(c_t); // 6

    // Total: trace_c(6) + det_a(1) + det_b(16) + det_c(16) + trace_ct(6) = 45
    return trace_c + det_a + det_b + det_c + trace_ct;
}
