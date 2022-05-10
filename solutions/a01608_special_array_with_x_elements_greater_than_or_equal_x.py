"""
Problem:
    1608. Special Array With X Elements Greater Than or Equal X
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x
Tags:
    Array, Binary Search, Sorting
Date:
    2022-05-10T14:11:52.140259+08:00
"""
from typing import List


class Solution(object):
    def specialArray(self, nums):
        nums = sorted(nums)
        for i in range(len(nums) + 1):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < i:
                    left = mid + 1
                if nums[mid] >= i:
                    right = mid - 1
            if len(nums) - left == i:
                return i
        return -1


tests = [
    (
        ([3, 5],
         ),
        2,
    ),
    (
        ([0, 0],
         ),
        -1,
    ),
    (
        ([0, 4, 3, 0, 4],
         ),
        3,
    ),
]
