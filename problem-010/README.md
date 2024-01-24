### Problem 10

**Summation of primes**

The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.

Find the sum of all the primes below two million.

---

**质数求和**

所有小于$10$的质数的和是$2 + 3 + 5 + 7 = 17$。

求所有小于两百万的质数的和。

---

answer code:

```python
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
```

---

answer code:

```python
#!/usr/bin/env python3

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

prime_list = generater_prime(upper_limit)
for i in prime_list:
    if i > upper_limit:
        break
    else:
        sum_of_primes = sum_of_primes + i

print("ans:", sum_of_primes)
```
