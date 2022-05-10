"""
Problem:
    1281. Subtract the Product and Sum of Digits of an Integer
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
Tags:
    Math
Date:
    2022-05-10T14:09:42.093699+08:00
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list_n = [int(x) for x in str(n)]
        pro_i = 1
        sum_i = 0
        for x in list_n:
            pro_i *= x
            sum_i += x
        return pro_i - sum_i


tests = [
    (
        (234,
         ),
        15,
    ),
    (
        (4421,
         ),
        21,
    ),
]
