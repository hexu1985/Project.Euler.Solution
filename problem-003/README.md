### Problem 3

**Largest prime factor**

The prime factors of $13195$ are $5$, $7$, $13$ and $29$.

What is the largest prime factor of the number $600851475143$?

---

**最大质因数**

$13195$的质因数包括$5$、$7$、$13$和$29$。

$600851475143$的最大质因数是多少？

---

answer code:

```python
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
```
