"""
Problem:
    485. Max Consecutive Ones
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/max-consecutive-ones
Tags:
    Array
Date:
    2022-05-10T14:05:14.338888+08:00
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans_list = []
        for num in nums:
            if num == 1:
                count += 1
            else:
                ans_list.append(count)
                count = 0
        ans_list.append(count)
        return max(ans_list)


tests = [
    (
        ([1, 1, 0, 1, 1, 1],
         ),
        3,
    ),
    (
        ([1, 0, 1, 1, 0, 1],
         ),
        2,
    ),
]
