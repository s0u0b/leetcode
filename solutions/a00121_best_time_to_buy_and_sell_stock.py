"""
Problem:
    121. Best Time to Buy and Sell Stock
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock
Tags:
    Array, Dynamic Programming
Date:
    2022-05-10T14:03:00.331874+08:00
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_low_price = prices[0]
        maximum_profit = 0
        for i, price in enumerate(prices):
            if price < current_low_price:
                current_low_price = price
            maximum_profit = max(price - current_low_price, maximum_profit)
        return maximum_profit


tests = [
    (
        ([7, 1, 5, 3, 6, 4],
         ),
        5,
    ),
    (
        ([7, 6, 4, 3, 1],
         ),
        0,
    ),
]
