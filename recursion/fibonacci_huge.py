#! /usr/bin/env python

# def get_fibonacci_huge_naive(n, m):
    # if n <= 1:
        # return n
# 
    # previous = 0
    # current  = 1
# 
    # for _ in range(n - 1):
        # previous, current = current, previous + current
# 
    # return current % m
# 

def get_pisano_period(m):
    prev, cur= 0, 1
    for i in range(0, m*m):
        prev, cur = cur, (prev + cur) %m 
        if (prev == 0 and cur == 1):
            return i+1 

def get_fib_huge_better(n, m):
    n = n %(get_pisano_period(m))

    if n <= 1:
        return n

    prev, cur = 0, 1
    for _ in range(n-1):
        prev, cur = cur, prev + cur
    return cur % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fib_huge_better(n, m))
