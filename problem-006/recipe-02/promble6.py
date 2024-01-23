#!/usr/bin/env python3

def square_then_sum(n):
    return n*(n+1)*(2*n+1)//6

def sum_then_square(n):
    return (n*(n+1)//2)**2

n = 100
ans = sum_then_square(n) - square_then_sum(n)
print("ans:", ans)

