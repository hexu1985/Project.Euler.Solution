#!/usr/bin/env python3

import time

def is_relatively_prime(prime_list, n):
    for i in prime_list:
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

def generater_prime(upper_limit):
    prime_list = [2, 3, 5, 7, 11, 13]
    if upper_limit < prime_list[-1]:
        return prime_list

    start = 2
    end = prime_list[-1]+1
    while True:
        start = end
        end = prime_list[-1]**2
        for i in range(start, end):
            if i > upper_limit:
                return prime_list
            else:
                if is_relatively_prime(prime_list, i):
                    prime_list.append(i)

upper_limit = 2000000
sum_of_primes = 0

tic = time.time()
prime_list = generater_prime(upper_limit)
sum_of_primes = sum(prime_list)
toc = time.time()

print("ans:", sum_of_primes)
print("use time:", toc-tic, "sec")

