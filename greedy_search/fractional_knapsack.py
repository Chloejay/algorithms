#! /usr/bin/env python 
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.

    weight_value_pairs = sorted(
        [Items(v, w) for v, w in zip(values, weights)], 
        key=lambda i: i.value / i.weight, reverse=True
    )

    space_left = int(capacity)
    for item in weight_value_pairs:

        if space_left - item.weight >= 0:
            value += item.value
            space_left -= item.weight

        else:
            value += (item.value / item.weight) * space_left
            space_left = 0

        if not space_left:
            break
    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
