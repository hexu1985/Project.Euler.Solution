#!/usr/bin/env python3

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        else:
            i = i + 1

    return True

sum_of_primes = 0
upper_limit = 2000000

for i in range(upper_limit):
    if is_prime(i):
        sum_of_primes = sum_of_primes + i

print("ans:", sum_of_primes)

