"""
Problem:
    1217. Minimum Cost to Move Chips to The Same Position
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position
Tags:
    Array, Math, Greedy
Date:
    2022-05-10T14:09:22.039825+08:00
"""
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        even = 0
        for coin in position:
            if coin % 2:
                even += 1
            else:
                odd += 1
        return min(even, odd)


tests = [
    (
        ([1, 2, 3],
         ),
        1,
    ),
    (
        ([2, 2, 2, 3, 3],
         ),
        2,
    ),
    (
        ([1, 1000000000],
         ),
        1,
    ),
]
