"""
Problem:
    396. Rotate Function
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/rotate-function
Tags:
    Array, Math, Dynamic Programming
Date:
    2022-05-10T14:05:03.938886+08:00
"""
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        nums_len = len(nums)
        if nums_len == 1:
            return 0

        sum_of_nums = sum(nums)
        f0 = sum([i * num for i, num in enumerate(nums)])
        max_sum = f0
        for i in range(len(nums) - 1, 0, -1):
            f0 += sum_of_nums - nums[i] * nums_len
            max_sum = max(max_sum, f0)
        return max_sum


tests = [
    (
        ([4, 3, 2, 6],
         ),
        26,
    ),
    (
        ([100],
         ),
        0,
    ),
]
