#!/usr/bin/env python3

import pdb

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

class ProductMemo:
    def __init__(self, digits_str, n):
        self.digits_str = digits_str[0:n]
        self.n_factors = n
        self.product_memo = dict()
        self._first_product()

    def _first_product(self):
        curr_digits_str = ""
        curr_product = 1
        n = self.n_factors
        for i in range(n):
            curr_product = curr_product * int(self.digits_str[n-1-i])
            curr_digits_str = self.digits_str[n-1-i] + curr_digits_str
            self.product_memo[curr_digits_str] = curr_product
        self.max_product = curr_product
        self.max_product_digits_str = curr_digits_str

    def update_product(self, digit_char):
        assert len(digit_char) == 1
        new_product_memo = dict()
        new_product_memo[digit_char] = int(digit_char)
        n = self.n_factors
        for i in range(1, n):
            sub_digits_str = self.digits_str[i:]
            sub_product = self.product_memo[sub_digits_str]
            curr_digits_str = sub_digits_str+digit_char
            curr_product = sub_product*int(digit_char)
            new_product_memo[curr_digits_str] = curr_product
        self.digits_str = self.digits_str[1:]+digit_char
        self.product_memo = new_product_memo
        if self.product_memo[self.digits_str] > self.max_product:
            self.max_product = self.product_memo[self.digits_str]
            self.max_product_digits_str = self.digits_str

    def get_result(self):
        return self.max_product, self.max_product_digits_str

n_factors = 13
product_memo = ProductMemo(digits_str, n_factors)

for i in range(n_factors, len(digits_str)):
    product_memo.update_product(digits_str[i])

max_product, max_product_digits_str = product_memo.get_result()
print("max_product:", max_product)
print("max_product_factor_list:", list(max_product_digits_str))
