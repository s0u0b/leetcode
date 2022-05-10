"""
Problem:
    1351. Count Negative Numbers in a Sorted Matrix
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
Tags:
    Array, Binary Search, Matrix
Date:
    2022-05-10T14:10:17.078380+08:00
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        a = [i for g in grid for i in g]
        for i in a:
            if i < 0:
                ans += 1
        return ans


tests = [
    (
        ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
         ),
        8,
    ),
    (
        ([[3, 2], [1, 0]],
         ),
        0,
    ),
]
