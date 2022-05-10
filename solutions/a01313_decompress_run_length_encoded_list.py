"""
Problem:
    1313. Decompress Run-Length Encoded List
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/decompress-run-length-encoded-list
Tags:
    Array
Date:
    2022-05-10T14:10:00.749821+08:00
"""
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        times = 0
        for (i, x) in enumerate(nums):
            if i % 2 == 0:
                times = x
            else:
                for t in range(times):
                    ans.append(x)
        return ans


tests = [
    (
        ([1, 2, 3, 4],
         ),
        [2, 4, 4, 4],
    ),
    (
        ([1, 1, 2, 3],
         ),
        [1, 3, 3],
    ),
]
