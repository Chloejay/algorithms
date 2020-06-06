#! /usr/bin/env python

"""Sorting entire array then do product.
"""

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    new_numbers = list()

    for i in numbers:
        new_numbers.append(i)
    return sorted(new_numbers)[n-1] *sorted(new_numbers)[n-2] 


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))