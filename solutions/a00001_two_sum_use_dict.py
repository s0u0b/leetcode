"""
Problem:
    1. Two Sum
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/two-sum
Tags:
    Array, Hash Table
Date:
    2022-05-10T14:00:29.877163+08:00
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}
        for index, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in nums_index:
                return [nums_index[num2], index]
            else:
                nums_index[num1] = index


tests = [
    (
        ([2, 7, 11, 15], 9,
         ),
        [0, 1],
    ),
    (
        ([3, 2, 4], 6,
         ),
        [1, 2],
    ),
    (
        ([3, 3], 6,
         ),
        [0, 1],
    ),
]
