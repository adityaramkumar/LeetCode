// Runtime: 172 ms, faster than 49.76% of C online submissions for Print in Order.
// Memory Usage: 6.2 MB, less than 100.00% of C online submissions for Print in Order.
// Difficulty: Easy

#include <semaphore.h>

typedef struct {
    // User defined data may be declared here.
    sem_t sema1, sema2;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    
    // Initialize user defined data here.
    sem_init(&(obj->sema1), 0, 0);
    sem_init(&(obj->sema2), 0, 0);
    return obj;
}

void first(Foo* obj) {
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    sem_post(&(obj->sema1));
}

void second(Foo* obj) {
    // printSecond() outputs "second". Do not change or remove this line.
    sem_wait(&(obj->sema1));
    printSecond();
    sem_post(&(obj->sema2));
}

void third(Foo* obj) {
    // printThird() outputs "third". Do not change or remove this line.
    sem_wait(&(obj->sema2));
    printThird();
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    sem_destroy(&(obj->sema1));
    sem_destroy(&(obj->sema2));
}
