"""
Problem:
    441. Arranging Coins
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/arranging-coins
Tags:
    Math, Binary Search
Date:
    2022-05-10T14:05:06.395758+08:00
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        sum_i = 0
        i = 0
        for i in range(1, n + 1):
            sum_i += i
            if sum_i > n:
                break
        return i - 1


tests = [
    (
        (5,
         ),
        2,
    ),
    (
        (8,
         ),
        3,
    ),
]
