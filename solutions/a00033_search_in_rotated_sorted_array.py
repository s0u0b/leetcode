"""
Problem:
    33. Search in Rotated Sorted Array
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/search-in-rotated-sorted-array
Tags:
    Array, Binary Search
Date:
    2022-05-10T18:45:58.274490+08:00
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            if nums[left] < target < nums[mid]:
                right = mid - 1
            elif nums[mid] < target < nums[right]:
                left = mid + 1
            elif nums[left] > nums[mid] > target:
                right = mid - 1
            elif nums[left] > target > nums[mid]:
                left = mid + 1
            elif target > nums[left] > nums[mid]:
                right = mid - 1
            elif nums[mid] > nums[left] > target:
                left = mid + 1
            elif target > nums[mid] > nums[left]:
                left = mid + 1
            elif nums[left] > target:
                return -1
            elif target > nums[right]:
                return -1
        return -1


tests = [
    (
        ([4, 5, 6, 7, 0, 1, 2], 0,
         ),
        4,
    ),
    (
        ([4, 5, 6, 7, 0, 1, 2], 3,
         ),
        -1,
    ),
    (
        ([1], 0,
         ),
        -1,
    ),
    (
        ([1, 3], 1,),
        0,
    ),
    (
        ([1, 3], 3,),
        1,
    ),
    (
        ([3, 1], 3,),
        0,
    ),
    (
        ([1, 3, 5], 5,),
        2,
    ),
    (
        (
            [1], 1,
        ),
        0,
    ),
    (
        ([1, 3], 0,
         ),
        -1,
    ),
]
