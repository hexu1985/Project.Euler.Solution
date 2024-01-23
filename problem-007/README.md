### Problem 7

10001st prime

By listing the first six prime numbers:
$2$, $3$, $5$, $7$, $11$, and $13$, we can see that the 6th prime is $13$.

What is the 10001st prime number?

---

第10001个质数

前6个质数分别是$2$、$3$、, $5$、$7$、$11$和$13$。

第10001个质数是多少？

---

answer code:

```python
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
```

