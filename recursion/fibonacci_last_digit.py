#! /usr/bin/env python

import sys

# def get_fibonacci_last_digit_naive(n):
    # if n <= 1:
        # return n
# 
    # previous = 0
    # current  = 1
# 
    # for _ in range(n - 1):
        # previous, current = current, previous + current
        # print(previous, current)
# 
    # return current % 10

def get_fib_better(n):
    if n <= 1:
        return n 
    else:
        for _ in range(n-1):

            result = get_fib_better(n-1) + get_fib_better(n-2)
        # module by 10 to get last digit of return value
        return result % 10

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_better(n))
