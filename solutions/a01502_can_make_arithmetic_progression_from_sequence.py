"""
Problem:
    1502. Can Make Arithmetic Progression From Sequence
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence
Tags:
    Array, Sorting
Date:
    2022-05-10T14:11:31.470845+08:00
"""
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) <= 2:
            return True
        diff = arr[0] - arr[1]
        for i in range(len(arr) - 1):
            if arr[i] - arr[i + 1] != diff:
                return False
        else:
            return True


tests = [
    (
        ([3, 5, 1],
         ),
        True,
    ),
    (
        ([1, 2, 4],
         ),
        False,
    ),
]
