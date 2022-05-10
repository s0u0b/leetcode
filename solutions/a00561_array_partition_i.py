"""
Problem:
    561. Array Partition I
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/array-partition-i
Tags:
    Array, Greedy, Sorting, Counting Sort
Date:
    2022-05-10T14:06:24.901894+08:00
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = sum(nums[1::2])
        return ans


tests = [
    (
        ([1, 4, 3, 2],
         ),
        4,
    ),
    (
        ([6, 2, 6, 5, 1, 2],
         ),
        9,
    ),
]
