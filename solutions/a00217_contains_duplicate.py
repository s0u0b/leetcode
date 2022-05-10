"""
Problem:
    217. Contains Duplicate
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/contains-duplicate
Tags:
    Array, Hash Table, Sorting
Date:
    2022-05-10T14:04:28.358765+08:00
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


tests = [
    (
        ([1, 2, 3, 1],
         ),
        True,
    ),
    (
        ([1, 2, 3, 4],
         ),
        False,
    ),
    (
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
         ),
        True,
    ),
]
