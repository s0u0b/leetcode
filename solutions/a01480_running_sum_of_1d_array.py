"""
Problem:
    1480. Running Sum of 1d Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/running-sum-of-1d-array
Tags:
    Array, Prefix Sum
Date:
    2022-05-10T14:11:20.645126+08:00
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i, n in enumerate(nums):
            if i == 0:
                ans.append(n)
            else:
                ans.append(ans[i - 1] + n)
        return ans


tests = [
    (
        ([1, 2, 3, 4],
         ),
        [1, 3, 6, 10],
    ),
    (
        ([1, 1, 1, 1, 1],
         ),
        [1, 2, 3, 4, 5],
    ),
    (
        ([3, 1, 2, 10, 1],
         ),
        [3, 4, 6, 16, 17],
    ),
]
