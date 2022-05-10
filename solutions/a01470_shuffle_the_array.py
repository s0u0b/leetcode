"""
Problem:
    1470. Shuffle the Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/shuffle-the-array
Tags:
    Array
Date:
    2022-05-10T14:11:10.684381+08:00
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            if i == n:
                break
            ans.append(num)
            ans.append(nums[n + i])
        return ans


tests = [
    (
        ([2, 5, 1, 3, 4, 7], 3,
         ),
        [2, 3, 5, 4, 1, 7],
    ),
    (
        ([1, 2, 3, 4, 4, 3, 2, 1], 4,
         ),
        [1, 4, 2, 3, 3, 2, 4, 1],
    ),
    (
        ([1, 1, 2, 2], 2,
         ),
        [1, 2, 1, 2],
    ),
]
