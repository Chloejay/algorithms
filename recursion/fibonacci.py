#! /usr/bin/env python 

def calc_fib(n):
    
    if (n <= 1):
        return n
    
    fib_list = list() 
    for i in range(0, n+1):
        if i<= 1:
            cur = i
        
        else:
            cur = fib_list[i-1] + fib_list[i-2]
        fib_list.append(cur)
    
    return fib_list[-1] 

if __name__ == "__main__":
    n = int(input())
    print(calc_fib(n))
    print(calc_fib2(n))