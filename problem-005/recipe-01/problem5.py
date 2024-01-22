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

def union_prime_factors(factors1, factors2):
    idx1 = 0
    idx2 = 0
    union_list = []
    while idx1 < len(factors1) and idx2 < len(factors2):
        if factors1[idx1] < factors2[idx2]:
            union_list.append(factors1[idx1])
            idx1 = idx1 + 1
        elif factors2[idx2] < factors1[idx1]:
            union_list.append(factors2[idx2])
            idx2 = idx2 + 1
        else:   # equal
            union_list.append(factors1[idx1])
            idx1 = idx1 + 1
            idx2 = idx2 + 1

    if idx1 < len(factors1):
        union_list.extend(factors1[idx1:])
    if idx2 < len(factors2):
        union_list.extend(factors2[idx2:])

    return union_list

union_factors = []
for i in range(1, 21):
    union_factors = union_prime_factors(union_factors, prime_factors(i))

ans = 1
for i in union_factors:
    ans = ans * i

print("ans:", ans)

