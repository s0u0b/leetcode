"""
Problem:
    35. Search Insert Position
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/search-insert-position
Tags:
    Array, Binary Search
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        else:
            return left


tests = [
    (
        ([1, 3, 5, 6], 5,
         ),
        2,
    ),
    (
        ([1, 3, 5, 6], 2,
         ),
        1,
    ),
    (
        ([1, 3, 5, 6], 7,
         ),
        4,
    ),
]
