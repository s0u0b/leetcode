"""
Problem:
    896. Monotonic Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/monotonic-array
Tags:
    Array
Date:
    2022-05-11T18:47:34.335645+08:00
"""
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)


tests = [
    (
        ([1, 2, 2, 3],
         ),
        True,
    ),
    (
        ([6, 5, 4, 4],
         ),
        True,
    ),
    (
        ([1, 3, 2],
         ),
        False,
    ),
]
