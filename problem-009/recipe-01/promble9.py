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


