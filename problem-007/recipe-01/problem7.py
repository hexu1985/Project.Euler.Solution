#!/usr/bin/env python3

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        else:
            i = i + 1

    return True

def nth_prime(nth):
    prime_list = [2, 3, 5, 7, 11, 13]
    if nth <= 6:
        return prime_list[nth]

    idx = 6
    n = 13
    while idx < nth:
        n = n + 1
        if is_prime(n):
            idx = idx + 1

    return n

ans = nth_prime(10001)
print("ans:", ans)
