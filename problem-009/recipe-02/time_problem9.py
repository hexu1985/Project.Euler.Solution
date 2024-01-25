#!/usr/bin/env python3

import sys
import time

the_sum = 1000

tic = time.time()
for a in range(1, the_sum//2):
    for b in range(a, the_sum-a):
        c = the_sum - a - b
        if c < a or c < b:
            break
        if a**2 + b**2 == c**2:
            toc = time.time()
            print("{}**2 + {}**2 = {}**2".format(a, b, c))
            print("ans:", a*b*c)
            print("use time:", toc-tic, "sec")
            sys.exit(1)


