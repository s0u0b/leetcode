"""
Problem:
    53. Maximum Subarray
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/maximum-subarray
Tags:
    Array, Divide and Conquer, Dynamic Programming
Date:
    2022-05-10T14:02:19.785871+08:00
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        sub_sum = float('-inf')
        for num in nums:
            sub_sum = max(num, num + sub_sum)
            max_sum = max(sub_sum, max_sum)
        return max_sum


tests = [
    (
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4],
         ),
        6,
    ),
    (
        ([1],
         ),
        1,
    ),
    (
        ([5, 4, -1, 7, 8],
         ),
        23,
    ),
]
