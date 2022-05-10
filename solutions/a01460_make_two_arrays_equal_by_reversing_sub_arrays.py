"""
Problem:
    1460. Make Two Arrays Equal by Reversing Sub-arrays
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays
Tags:
    Array, Hash Table, Sorting
Date:
    2022-05-10T14:11:04.664979+08:00
"""
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for t in target:
            if t in arr:
                arr.remove(t)
            else:
                return False
        else:
            if not arr:
                return True
            else:
                return False


tests = [
    (
        ([1, 2, 3, 4], [2, 4, 1, 3],
         ),
        True,
    ),
    (
        ([7], [7],
         ),
        True,
    ),
    (
        ([3, 7, 9], [3, 7, 11],
         ),
        False,
    ),
]
