#! /usr/bin/env python 

from typing import List, Tuple, Union
"""
Use sort, the worst case, time complexity is O(N(logN))
"""
def _2sum(lst: List[int], desired_sum: int)-> Union[None, Tuple[int, int]]:
    lst.sort() #sort the sequence 
    start = 0 #pos 0 
    end = len(lst)-1 #pos -1 
    while start < end:
        curr_sum = lst[start] + lst[end] 

        if curr_sum == desired_sum:
            return lst[start], lst[end]

        elif curr_sum > desired_sum:
            end -= 1 
        elif curr_sum < desired_sum:
            start += 1 
    return None

# another solution: using hash table
"""
Step 1: Build a hashtable, use hashtable key
Step 2: Hash table, the worst case, time complexity is O(N) to good worst one is O(1)
"""
def create_hashtable(lst: List[int])-> dict:
    hashtable = {}
    for num in lst:
        hashtable[num] = True

    return hashtable

def _2sum_v2(lst: List[int], desired_sum: int)-> Union[None, Tuple[int, int]]:
    hashtable= create_hashtable(lst)

    for num in lst:
        complement = desired_sum - num 
        if complement in hashtable.keys() -[num]: #remove duplicated one == num
            return num, complement 

    return None 




if __name__ == "__main__":
    list_= [1, 10, 21, 100, 2, 3, 4, 5, 20, 30, 6]
    res = _2sum(lst = list_, desired_sum = 101)
    print(res) if res is not None else print('Return None!')
    print(create_hashtable(list_))
    res_v2 = _2sum(lst = list_, desired_sum = 101)
    print(res_v2) if res is not None else print('Return None!')