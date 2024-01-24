### Problem 9

**Special Pythagorean triplet**

A Pythagorean triplet is a set of three natural numbers,
$a < b < c$, for which,

$$
a^2 + b^2 = c^2
$$

For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

There exists exactly one Pythagorean triplet for which $a + b + c = 1000$. 
Find the product $abc$.

---

**特殊毕达哥拉斯三元组**

毕达哥拉斯三元组由三个自然数$a < b < c$组成，并满足

$$
a^2 + b^2 = c^2
$$

例如，$3^2 + 4^2 = 9 + 16 = 25 = 5^2$。

有且只有一个毕达哥拉斯三元组满足$a + b + c = 1000$。
求这个三元组的乘积$abc$。

---

answer code:

```python
#!/usr/bin/env python3

import sys

the_sum = 1000

for a in range(1, the_sum):
    for b in range(a, the_sum-a):
        c = the_sum - a - b
        if c < a or c < b:
            continue
        if a**2 + b**2 == c**2:
            print("{}**2 + {}**2 = {}**2".format(a, b, c))
            print("ans:", a*b*c)
            sys.exit(1)
```

