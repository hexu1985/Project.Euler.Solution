#!/usr/bin/env python3

def square_then_sum(n):
    res = 0
    for i in range(n+1):
        res = res + i*i
    return res

def sum_then_square(n):
    res = sum(range(n+1))
    return res*res

n = 100
ans = sum_then_square(n) - square_then_sum(n)
print("ans:", ans)

