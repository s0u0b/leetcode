"""
Problem:
    704. Binary Search
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/binary-search
Tags:
    Array, Binary Search
Date:
    2022-05-10T14:07:43.258815+08:00
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
            return -1


tests = [
    (
        ([-1, 0, 3, 5, 9, 12], 9,),
        4,
    ),
    (
        ([-1, 0, 3, 5, 9, 12], 2,),
        -1,
    ),
    (
        ([1], 1,),
        0,
    ),
    (
        ([1], 0,),
        -1,
    ),
]
