### Problem 1

**Multiples of $3$ or $5$**

If we list all the natural numbers below $10$ that are multiples of $3$ or $5$ , we get $3, 5, 6$ and $9$ . 
The sum of these multiples is $23$.

Find the sum of all the multiples of $3$ or $5$ below $1000$.

---

**$3$或$5$的倍数**

在小于$10$的自然数中，$3$或$5$的倍数有$3$、$5$、$6$和$9$，这些数之和是$23$。

求小于$1000$的自然数中所有$3$或$5$的倍数之和。

---

answer code:

```python
#!/usr/bin/env python3

ans=0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        ans += i
print("ans:", ans)
```
