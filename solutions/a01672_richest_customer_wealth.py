"""
Problem:
    1672. Richest Customer Wealth
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/richest-customer-wealth
Tags:
    Array, Matrix
Date:
    2022-05-10T14:11:59.168845+08:00
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum_wealth = 0
        customer_wealth = 0
        for account in accounts:
            for wealth in account:
                customer_wealth += int(wealth)
            if customer_wealth >= maximum_wealth:
                maximum_wealth = customer_wealth
            customer_wealth = 0
        return maximum_wealth


tests = [
    (
        ([[1, 2, 3], [3, 2, 1]],
         ),
        6,
    ),
    (
        ([[1, 5], [7, 3], [3, 5]],
         ),
        10,
    ),
    (
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]],
         ),
        17,
    ),
]
