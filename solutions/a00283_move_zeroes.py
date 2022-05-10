"""
Problem:
    283. Move Zeroes
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/move-zeroes
Tags:
    Array, Two Pointers
Date:
    2022-05-10T14:04:41.894115+08:00
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for index, num in enumerate(nums):
            if num != 0:
                nums[cur] = num
                cur += 1
                if index >= cur:
                    nums[index] = 0


tests = [
    (
        ([0, 1, 0, 3, 12],
         ),
        [1, 3, 12, 0, 0],
    ),
    (
        ([0],
         ),
        [0],
    ),
]


def validator(moveZeroes, inputs, expected):
    nums = inputs[0]
    moveZeroes(nums)
    assert nums == expected, (nums, expected)
