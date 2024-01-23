### Problem 6

**Sum square difference**

The sum of the squares of the first ten natural numbers is,

$$
1^2 + 2^2 + \cdots + 10^2 = 385
$$

The square of the sum of the first ten natural numbers is,

$$
(1 + 2 + \cdots + 10)^2 = 3025
$$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 285 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

---

**平方和与和平方之差**

前十个自然数的平方的和是

$$
1^2 + 2^2 + \cdots + 10^2 = 385
$$

前十个自然数的和的平方是

$$
(1 + 2 + \cdots + 10)^2 = 3025
$$

因此，前十个自然数的平方和与和平方之差是$3025 - 285 = 2640$。

求前一百个自然数的平方的与和平方之差。

---

answer code:

```python
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
```

---

answer code:

```python
#!/usr/bin/env python3

def square_then_sum(n):
    return n*(n+1)*(2*n+1)//6

def sum_then_square(n):
    return (n*(n+1)//2)**2

n = 100
ans = sum_then_square(n) - square_then_sum(n)
print("ans:", ans)
```

---

answer code:

```python
#!/usr/bin/env python3

n = 100
ans = n*(n**2-1)*(3*n+2)//12
print("ans:", ans)
```

