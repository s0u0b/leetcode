"""
Problem:
    26. Remove Duplicates from Sorted Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/remove-duplicates-from-sorted-array
Tags:
    Array, Two Pointers
Date:
    2022-05-10T14:00:29.877163+08:00
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            while nums.count(num) > 1:
                nums.remove(num)
        return len(nums)


tests = [
    (
        ([1, 1, 2],
         ),
        2,
    ),
    (
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
         ),
        5,
    ),
]
