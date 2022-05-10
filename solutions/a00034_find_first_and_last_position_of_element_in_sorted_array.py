"""
Problem:
    34. Find First and Last Position of Element in Sorted Array
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
Tags:
    Array, Binary Search
Date:
    2022-05-10T14:00:29.877163+08:00
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(num_list, target_num):
            left, right = 0, len(num_list) - 1
            while left <= right:
                mid = (left + right) // 2
                if num_list[mid] == target_num:
                    return mid
                if target_num < num_list[mid]:
                    right = mid - 1
                if num_list[mid] <= target_num:
                    left = mid + 1
            return -1

        mid_index = binary_search(nums, target)
        if mid_index == -1:
            return [-1, -1]

        left_index = right_index = mid_index
        if binary_search(nums[:mid_index], target) != -1:
            while binary_search(nums[:left_index], target) != -1:
                left_index = binary_search(nums[:left_index], target)
        while binary_search(nums[right_index:], target) != -1:
            right_index += 1
        return [left_index, right_index - 1]


tests = [
    (
        ([5, 7, 7, 8, 8, 10], 8,
         ),
        [3, 4],
    ),
    (
        ([5, 7, 7, 8, 8, 10], 6,
         ),
        [-1, -1],
    ),
    (
        ([], 0,
         ),
        [-1, -1],
    ),
]
