// Runtime: 348 ms, faster than 52.94% of C online submissions for Print FooBar Alternately.
// Memory Usage: 7.1 MB, less than 100.00% of C online submissions for Print FooBar Alternately.
// Difficulty: Medium

#include <semaphore.h>

typedef struct {
    int n;
    sem_t sema_foo, sema_bar;
} FooBar;

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    sem_init(&(obj->sema_foo), 0, 1);
    sem_init(&(obj->sema_bar), 0, 0);
    return obj;
}

void foo(FooBar* obj) {
    for (int i = 0; i < obj->n; i++) {
        // printFoo() outputs "foo". Do not change or remove this line.
        sem_wait(&(obj->sema_foo));
        printFoo();
        sem_post(&(obj->sema_bar));
    }
}

void bar(FooBar* obj) {
    for (int i = 0; i < obj->n; i++) {
        // printBar() outputs "bar". Do not change or remove this line.
        sem_wait(&(obj->sema_bar));
        printBar();
        sem_post(&(obj->sema_foo));
    }
}

void fooBarFree(FooBar* obj) {
    
}
