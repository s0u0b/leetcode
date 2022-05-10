"""
Problem:
    1512. Number of Good Pairs
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/number-of-good-pairs
Tags:
    Array, Hash Table, Math, Counting
Date:
    2022-05-10T14:11:34.506624+08:00
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i, num1 in enumerate(nums):
            for num2 in nums[i + 1:]:
                if num1 == num2:
                    ans = ans + 1
        return ans


tests = [
    (
        ([1, 2, 3, 1, 1, 3],
         ),
        4,
    ),
    (
        ([1, 1, 1, 1],
         ),
        6,
    ),
    (
        ([1, 2, 3],
         ),
        0,
    ),
]
