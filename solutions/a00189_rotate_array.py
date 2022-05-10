"""
Problem:
    189. Rotate Array
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/rotate-array
Tags:
    Array, Math, Two Pointers
Date:
    2022-05-10T14:03:08.361964+08:00
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())


tests = [
    (
        ([1, 2, 3, 4, 5, 6, 7], 3,
         ),
        [5, 6, 7, 1, 2, 3, 4],
    ),
    (
        ([-1, -100, 3, 99], 2,
         ),
        [3, 99, -1, -100],
    ),
]


def validator(rotate, inputs, expected):
    nums, k = inputs
    rotate(nums, k)
    assert nums == expected, (nums, expected)
