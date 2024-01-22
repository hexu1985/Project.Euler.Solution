#!/usr/bin/env python3

upper_limit = 4000000

fn_2 = 0
fn_1 = 1
fn = fn_1 + fn_2

ans = 0
while True:
    if fn >= upper_limit:
        break
    if fn % 2 == 0:
        ans += fn
    fn_2 = fn_1
    fn_1 = fn
    fn = fn_1 + fn_2

print("ans:", ans)

