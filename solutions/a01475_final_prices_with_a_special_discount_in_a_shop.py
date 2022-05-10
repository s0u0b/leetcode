"""
Problem:
    1475. Final Prices With a Special Discount in a Shop
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop
Tags:
    Array, Stack, Monotonic Stack
Date:
    2022-05-10T14:11:17.433430+08:00
"""
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i, price in enumerate(prices):
            for discount in prices[i + 1:]:
                if price >= discount:
                    ans.append(price - discount)
                    break
            else:
                ans.append(price)
        return ans


tests = [
    (
        ([8, 4, 6, 2, 3],
         ),
        [4, 2, 4, 2, 3],
    ),
    (
        ([1, 2, 3, 4, 5],
         ),
        [1, 2, 3, 4, 5],
    ),
    (
        ([10, 1, 1, 6],
         ),
        [9, 0, 1, 6],
    ),
]
