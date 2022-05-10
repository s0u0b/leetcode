"""
Problem:
    852. Peak Index in a Mountain Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/peak-index-in-a-mountain-array
Tags:
    Array, Binary Search
Date:
    2022-05-10T14:08:15.453618+08:00
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid - 1] < arr[mid]:
                left = mid
            if arr[mid] > arr[mid + 1]:
                right = mid
        else:
            return left


tests = [
    (
        ([0, 1, 0],
         ),
        1,
    ),
    (
        ([0, 2, 1, 0],
         ),
        1,
    ),
    (
        ([0, 10, 5, 2],
         ),
        1,
    ),
]
