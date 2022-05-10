"""
Problem:
    1365. How Many Numbers Are Smaller Than the Current Number
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
Tags:
    Array, Hash Table, Sorting, Counting
Date:
    2022-05-10T14:10:23.055314+08:00
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            count = 0
            for k in nums:
                if n > k:
                    count = count + 1
            ans = ans + [count]
        return ans


tests = [
    (
        ([8, 1, 2, 2, 3],
         ),
        [4, 0, 1, 1, 3],
    ),
    (
        ([6, 5, 4, 8],
         ),
        [2, 1, 0, 3],
    ),
    (
        ([7, 7, 7, 7],
         ),
        [0, 0, 0, 0],
    ),
]
