// SPDX-License-Identifier: MIT
// Copyright (c) 2020-2026 Takayuki Nagata
// Cooperative Mini-RTOS Task Scheduler Test Program for Hack CPU

#define MAX_TASKS 4
#define TASK_READY 1
#define TASK_BLOCKED 2
#define TASK_COMPLETED 3

typedef struct Task {
    int id;
    int state;
    int counter;
    void (*task_func)(struct Task *self);
} Task;

typedef struct Scheduler {
    Task tasks[MAX_TASKS];
    int num_tasks;
    int current_task;
    int shared_mailbox;
} Scheduler;

// Task 1: Producer task (increments counter and writes to mailbox)
__attribute__((noinline)) void task_producer(Task *self) {
    self->counter += 10;
    if (self->counter >= 30) {
        self->state = TASK_COMPLETED;
    }
}

// Task 2: Consumer task (reads from producer and computes)
__attribute__((noinline)) void task_consumer(Task *self) {
    self->counter += 5;
    if (self->counter >= 15) {
        self->state = TASK_COMPLETED;
    }
}

// Task 3: Math worker task (multiplies & computes)
__attribute__((noinline)) void task_worker(Task *self) {
    self->counter = (self->counter * 3) + 1;
    self->state = TASK_COMPLETED;
}

__attribute__((noinline)) void scheduler_init(Scheduler *sched) {
    sched->num_tasks = 3;
    sched->current_task = 0;
    sched->shared_mailbox = 0;

    sched->tasks[0].id = 1;
    sched->tasks[0].state = TASK_READY;
    sched->tasks[0].counter = 0;
    sched->tasks[0].task_func = task_producer;

    sched->tasks[1].id = 2;
    sched->tasks[1].state = TASK_READY;
    sched->tasks[1].counter = 0;
    sched->tasks[1].task_func = task_consumer;

    sched->tasks[2].id = 3;
    sched->tasks[2].state = TASK_READY;
    sched->tasks[2].counter = 4;
    sched->tasks[2].task_func = task_worker;
}

__attribute__((noinline)) int scheduler_run(Scheduler *sched) {
    int active_tasks = sched->num_tasks;
    int cycles = 0;

    while (active_tasks > 0 && cycles < 50) {
        cycles++;
        Task *t = &sched->tasks[sched->current_task];

        if (t->state == TASK_READY) {
            // Invoke task function via function pointer
            t->task_func(t);

            if (t->state == TASK_COMPLETED) {
                active_tasks--;
            }
        }

        sched->current_task = (sched->current_task + 1) % sched->num_tasks;
    }

    int total_score = sched->tasks[0].counter + sched->tasks[1].counter + sched->tasks[2].counter;
    return total_score; // 30 + 15 + 13 = 58
}

int main(void) {
    Scheduler sched;
    scheduler_init(&sched);
    return scheduler_run(&sched); // Expect 58
}
