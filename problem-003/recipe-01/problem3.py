#!/usr/bin/env python3

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n = n // i
            factors.append(i)
        else:
            i = i + 1
    if n > 1:
        factors.append(n)
    return factors

n = 600851475143
factors = prime_factors(n)
ans = factors[len(factors)-1]
print("ans:", ans)
