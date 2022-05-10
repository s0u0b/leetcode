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
        for i, num in enumerate(nums):
            if target - num in nums[i + 1:]:
                return [i, nums.index(target - num, i + 1)]


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
