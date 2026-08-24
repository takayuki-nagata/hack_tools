// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Stack-Based String Parsing & Numeric Conversion Test Program for Hack CPU

__attribute__((noinline)) int is_digit(int ch) {
    if (ch >= '0') {
        if (ch <= '9') {
            return ch - '0';
        }
    }
    return -1;
}

__attribute__((noinline)) int is_op(int ch) {
    if (ch == '+') return 1;
    if (ch == '-') return 2;
    if (ch == '*') return 3;
    return 0;
}

__attribute__((noinline)) int my_strlen(const int *s) {
    int len = 0;
    while (s[len] != 0) {
        len++;
    }
    return len;
}

__attribute__((noinline)) int my_atoi(const int *s) {
    int res = 0;
    int sign = 1;
    int i = 0;

    while (s[i] == ' ' || s[i] == '\t') {
        i++;
    }

    if (s[i] == '-') {
        sign = -1;
        i++;
    } else if (s[i] == '+') {
        i++;
    }

    while (s[i] != 0) {
        int d = is_digit(s[i]);
        if (d < 0) break;
        res = res * 10 + d;
        i++;
    }
    return res * sign;
}

__attribute__((noinline)) int my_itoa(int val, int *buf) {
    int i = 0;
    int is_neg = 0;
    unsigned int v;

    if (val < 0) {
        is_neg = 1;
        v = (unsigned int)(-val);
    } else {
        v = (unsigned int)val;
    }

    if (v == 0) {
        buf[i++] = '0';
        buf[i] = 0;
        return i;
    }

    int temp[8];
    int t_idx = 0;
    while (v > 0) {
        temp[t_idx++] = '0' + (int)(v % 10);
        v /= 10;
    }

    if (is_neg) {
        buf[i++] = '-';
    }

    while (t_idx > 0) {
        buf[i++] = temp[--t_idx];
    }
    buf[i] = 0;
    return i;
}

__attribute__((noinline)) int eval_simple_expr(const int *s) {
    int acc = 0;
    int i = 0;
    int op = '+';

    while (s[i] != 0) {
        while (s[i] == ' ') i++;
        if (s[i] == 0) break;

        int op_type = is_op(s[i]);
        if (op_type != 0) {
            op = s[i];
            i++;
            continue;
        }

        int num = 0;
        while (s[i] != 0) {
            int d = is_digit(s[i]);
            if (d < 0) break;
            num = num * 10 + d;
            i++;
        }

        if (op == '+') acc += num;
        else if (op == '-') acc -= num;
        else if (op == '*') acc *= num;
    }
    return acc;
}

int main(void) {
    // 1. Test atoi:
    // Build "-420" on stack buffer
    int s1[8];
    s1[0] = ' '; s1[1] = ' '; s1[2] = '-'; s1[3] = '4'; s1[4] = '2'; s1[5] = '0'; s1[6] = 0;
    int n1 = my_atoi(s1); // -420

    int s2[8];
    s2[0] = '1'; s2[1] = '0'; s2[2] = '2'; s2[3] = '4'; s2[4] = 0;
    int n2 = my_atoi(s2); // 1024

    // 2. Test itoa:
    int s3[8];
    int len3 = my_itoa(-789, s3); // 4
    int n3 = my_atoi(s3);         // -789

    // 3. Test simple expression evaluator:
    // "10 + 20 * 3 - 15" -> (10 + 20) * 3 - 15 = 90 - 15 = 75
    int expr[32];
    expr[0] = '1'; expr[1] = '0'; expr[2] = ' ';
    expr[3] = '+'; expr[4] = ' ';
    expr[5] = '2'; expr[6] = '0'; expr[7] = ' ';
    expr[8] = '*'; expr[9] = ' ';
    expr[10] = '3'; expr[11] = ' ';
    expr[12] = '-'; expr[13] = ' ';
    expr[14] = '1'; expr[15] = '5'; expr[16] = 0;

    int eval_res = eval_simple_expr(expr); // 75

    // Total:
    // n1(-420) + n2(1024) + len3(4) + n3(-789) + eval_res(75)
    // = -420 + 1024 + 4 - 789 + 75 = -106
    return n1 + n2 + len3 + n3 + eval_res;
}
