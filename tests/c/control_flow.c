// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Complex Control Flow, Short-Circuit Logic & State Machine Test Program for Hack CPU

__attribute__((noinline)) int test_short_circuit(int a, int b, int c, int d, int e) {
    int flag = 0;
    // Condition 1: Short-circuit OR
    if (a > 10 || b++ > 5) {
        flag += 10;
    }
    // Condition 2: Short-circuit AND
    if (c == 0 && d++ > 0) {
        flag += 20;
    }
    // Condition 3: Nested boolean logic
    if (!(a <= b) && (c < d || e == 100)) {
        flag += 40;
    }
    return flag + b + d;
}

__attribute__((noinline)) int test_nested_loops_goto(void) {
    int total = 0;
    for (int i = 0; i < 10; i++) {
        if (i == 2)
            continue;
        if (i == 8)
            break;

        for (int j = 0; j < 5; j++) {
            if (j == 3)
                continue;
            if (i == 5 && j == 2)
                goto jump_out;
            total += i * 10 + j;
        }
    }

jump_out:
    return total;
}

__attribute__((noinline)) int test_ternary_chain(int val) {
    return val > 100 ? 1 : val > 50 ? 2 : val > 20 ? 3 : val > 0 ? 4 : val == 0 ? 5 : -1;
}

typedef enum State { ST_IDLE = 0, ST_INIT, ST_RUN, ST_PAUSE, ST_ERROR, ST_DONE } State;

__attribute__((noinline)) int test_state_machine(void) {
    State st = ST_IDLE;
    int data = 0;
    int steps = 0;

    while (st != ST_DONE && steps < 20) {
        steps++;
        switch (st) {
        case ST_IDLE:
            st = ST_INIT;
            data += 1;
            break;
        case ST_INIT:
            st = ST_RUN;
            data += 10;
            break;
        case ST_RUN:
            if (data < 35) {
                data += 10;
                st = ST_PAUSE;
            } else {
                st = ST_DONE;
            }
            break;
        case ST_PAUSE:
            data += 2;
            st = ST_RUN;
            break;
        default:
            st = ST_ERROR;
            break;
        }
    }
    return (data * 100) + steps;
}

int main(void) {
    // 1. Short-circuit:
    // a=15 (>10: true, b not incremented) -> flag += 10
    // c=1 (==0: false, d not incremented) -> flag no change
    // a(15) > b(3): true, c(1) < d(4): true -> flag += 40
    // flag=50, b=3, d=4 -> ret = 57
    int sc = test_short_circuit(15, 3, 1, 4, 99); // 57

    // 2. Nested loops + break/continue/goto:
    // i=0: j=0,1,2,4 -> (0,1,2,4) = 7
    // i=1: j=0,1,2,4 -> (10,11,12,14) = 47
    // i=2: skipped (continue)
    // i=3: j=0,1,2,4 -> (30,31,32,34) = 127
    // i=4: j=0,1,2,4 -> (40,41,42,44) = 167
    // i=5: j=0 (50), j=1 (51), j=2 (goto jump_out) = 101
    // Total = 7 + 47 + 127 + 167 + 101 = 449
    int loop = test_nested_loops_goto(); // 449

    // 3. Ternary chain:
    int t1 = test_ternary_chain(150);        // 1
    int t2 = test_ternary_chain(75);         // 2
    int t3 = test_ternary_chain(35);         // 3
    int t4 = test_ternary_chain(10);         // 4
    int t5 = test_ternary_chain(0);          // 5
    int t6 = test_ternary_chain(-10);        // -1
    int t_sum = t1 + t2 + t3 + t4 + t5 + t6; // 1 + 2 + 3 + 4 + 5 - 1 = 14

    // 4. State machine:
    // Step 1: IDLE -> INIT, data=1
    // Step 2: INIT -> RUN, data=11
    // Step 3: RUN -> PAUSE, data=21
    // Step 4: PAUSE -> RUN, data=23
    // Step 5: RUN -> PAUSE, data=33
    // Step 6: PAUSE -> RUN, data=35
    // Step 7: RUN -> DONE
    // Result = (35 * 100) + 7 = 3507
    int sm = test_state_machine(); // 3507

    // Total: sc(57) + loop(449) + t_sum(14) + sm(3507) = 4027
    return sc + loop + t_sum + sm;
}
