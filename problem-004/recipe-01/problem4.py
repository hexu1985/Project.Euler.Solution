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
