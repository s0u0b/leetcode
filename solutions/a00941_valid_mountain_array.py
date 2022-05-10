"""
Problem:
    941. Valid Mountain Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/valid-mountain-array
Tags:
    Array
Date:
    2022-05-10T14:08:27.990497+08:00
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mountain = max(arr)
        if arr.count(mountain) > 1:
            return False
        left = arr[:arr.index(mountain)]
        right = arr[arr.index(mountain) + 1:]
        left.sort()
        right.sort(reverse=True)
        if len(left) != len(set(left)):
            return False
        if len(right) != len(set(right)):
            return False
        if not left or not right:
            return False
        if left == arr[:arr.index(mountain)] and right == arr[arr.index(mountain) + 1:]:
            return True
        return False


tests = [
    (
        ([2, 1],
         ),
        False,
    ),
    (
        ([3, 5, 5],
         ),
        False,
    ),
    (
        ([0, 3, 2, 1],
         ),
        True,
    ),
]
