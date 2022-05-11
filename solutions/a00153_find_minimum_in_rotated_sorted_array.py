"""
Problem:
    153. Find Minimum in Rotated Sorted Array
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
Tags:
    Array, Binary Search
Date:
    2022-05-11T14:03:24.814175+08:00
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if len(nums) == 1:
            return min(nums)
        while left < right:
            mid = (left + right) // 2
            '''
            12345 
            51234 -> 512 -> 51
            45123 -> 451 -> 51
            34512 -> 512 -> 51
            23451 -> 451 -> 51
            '''
            if right - left == 1:
                return min(nums[left:right + 1])
            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            elif nums[left] > nums[right] > nums[mid]:
                right = mid
            elif nums[mid] > nums[left] > nums[right]:
                left = mid


tests = [
    (
        ([3, 4, 5, 1, 2],
         ),
        1,
    ),
    (
        ([4, 5, 6, 7, 0, 1, 2],
         ),
        0,
    ),
    (
        ([11, 13, 15, 17],
         ),
        11,
    ),
    (
        ([1],
         ),
        1,
    ),
]
