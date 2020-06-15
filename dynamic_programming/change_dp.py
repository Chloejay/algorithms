#! /usr/bin/env python 

import sys
from math import inf 
# DP: change and get optimized results for each stages of whole problem progress
# usage of `principle of optimality` and backward/forward induction

def get_change(m):
    # divede the problem into three different stages, for coins types of 1,3 4
    coins = [1, 3, 4]

    min_number_of_coins = [None] * (m + 1)

    min_number_of_coins[0] = 0

    for i in range(1, m + 1):
        min_number_of_coins[i] = inf
        for whole_coin in coins:
            if i >= whole_coin:
                tmp = min_number_of_coins[i - whole_coin] + 1
                if tmp < min_number_of_coins[i]:
                    min_number_of_coins[i] = tmp
            else:
                break
        return min_number_of_coins[m]

    return m // 4

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
