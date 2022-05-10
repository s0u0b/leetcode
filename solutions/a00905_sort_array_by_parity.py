"""
Problem:
    905. Sort Array By Parity
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/sort-array-by-parity
Tags:
    Array, Two Pointers, Sorting
Date:
    2022-05-10T14:08:24.952775+08:00
"""
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for a in A:
            if a % 2:
                even.append(a)
            else:
                odd.append(a)
        ans = odd + even
        return ans


tests = [
    (
        ([3, 1, 2, 4],
         ),
        [2, 4, 3, 1],
    ),
    (
        ([0],
         ),
        [0],
    ),
]
