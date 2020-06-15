#! /usr/bin/env python 

def get_change_navie(m):
    n = 0
    l = 0
    if m > 10:
        n += m//10 #how many coins
        l += m%10 #the remaining value 
        if l > 5:
            n += l//5
            l += l%5
            
    return n + l
# 
def get_change(m):
    # sort coins
    coins = [10, 5, 1] 
    # init value count 
    count = 0
    for coin in coins:
        count += m // coin
        m %= coin

    return count 
    
if __name__ == '__main__':
    m = int(input())
    print(get_change(m))