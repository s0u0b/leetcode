"""
Problem:
    1640. Check Array Formation Through Concatenation
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/check-array-formation-through-concatenation
Tags:
    Array, Hash Table
Date:
    2022-05-10T14:11:54.729467+08:00
"""
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        check_list = []
        for a in arr:
            check_list.append(a)
            if check_list in pieces:
                pieces.remove(check_list)
                check_list = []
        return not pieces


tests = [
    (
        ([15, 88], [[88], [15]],
         ),
        True,
    ),
    (
        ([49, 18, 16], [[16, 18, 49]],
         ),
        False,
    ),
    (
        ([91, 4, 64, 78], [[78], [4, 64], [91]],
         ),
        True,
    ),
]
