### Problem 4

**Largest palindrome product**

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two-digit numbers is $9009 = 91*99$.

Find the largest palindrome made from the product of two 3-digit numbers.

---

**最大回文乘积**

回文数是指从前往后读和从后往前读都一样的数。
由两个位数相乘得到的回文数中，最大的是$9009 = 91*99$。

求最大的由两个3位数相乘得到的回文数。

---

answer code:

```python
#!/usr/bin/env python3

def is_palindrome_str(s):
    beg = 0
    end = len(s)-1
    while beg < end:
        if s[beg] != s[end]:
            return False
        beg = beg + 1
        end = end - 1
    return True

def int_to_str(i):
    return str(i)

ans_i = 0
ans_j = 0
ans = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if is_palindrome_str(int_to_str(product)):
            if product > ans:
                ans = product
                ans_i = i
                ans_j = j

print("ans: {}={}*{}".format(ans, ans_i, ans_j))
```
