#!/usr/bin/env python3

from enum import Enum
import time

digits_str = (
            "73167176531330624919225119674426574742355349194934"
            "96983520312774506326239578318016984801869478851843"
            "85861560789112949495459501737958331952853208805511"
            "12540698747158523863050715693290963295227443043557"
            "66896648950445244523161731856403098711121722383113"
            "62229893423380308135336276614282806444486645238749"
            "30358907296290491560440772390713810515859307960866"
            "70172427121883998797908792274921901699720888093776"
            "65727333001053367881220235421809751254540594752243"
            "52584907711670556013604839586446706324415722155397"
            "53697817977846174064955149290862569321978468622482"
            "83972241375657056057490261407972968652414535100474"
            "82166370484403199890008895243450658541227588666881"
            "16427171479924442928230863465674813919123162824586"
            "17866458359124566529476545682848912883142607690042"
            "24219022671055626321111109370544217506941658960408"
            "07198403850962455444362981230987879927244284909188"
            "84580156166097919133875499200524063689912560717606"
            "05886116467109405077541002256983155200055935729725"
            "71636269561882670428252483600823257530420752963450"
            )

class Direction(Enum):
    up = 0
    down = 1


class ProductMemo:
    def __init__(self, digits_str, n):
        self.curr_direction = None
        self.digits_str = digits_str[0:n]
        self.local_maximum_list = [self.digits_str]

    def update_product(self, digit_char):
        assert len(digit_char) == 1
        new_digits_str = self.digits_str[1:]+digit_char
        if self.digits_str[0] <= digit_char:
            self.curr_direction = Direction.up
        else:   # self.digits_str[0] > digit_char
            if self.curr_direction == Direction.up:
                self.local_maximum_list.append(self.digits_str)
            self.curr_direction = Direction.down
        self.digits_str = new_digits_str

    def get_local_maximum_list(self):
        return self.local_maximum_list

def product(digits_str):
    res = 1
    for digit_char in digits_str:
        res = res * int(digit_char)
    return res

n_factors = 13
tic = time.time()
product_memo = ProductMemo(digits_str, n_factors)

for i in range(n_factors, len(digits_str)):
    product_memo.update_product(digits_str[i])

local_maximum_list = product_memo.get_local_maximum_list()
toc = time.time()

print("len(local_maximum_list):", len(local_maximum_list))

# last digits_str
max_product_sub_str = digits_str[len(digits_str)-n_factors:]
max_product = product(max_product_sub_str)
for curr_product_sub_str in local_maximum_list:
    curr_product = product(curr_product_sub_str)
    if curr_product > max_product:
        max_product = curr_product
        max_product_sub_str = curr_product_sub_str

print("max_product:", max_product)
print("max_product_sub_str:", max_product_sub_str)
print("use time:", toc-tic, "sec")
