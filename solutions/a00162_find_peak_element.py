"""
Problem:
    162. Find Peak Element
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/find-peak-element
Tags:
    Array, Binary Search
Date:
    2022-05-11T18:26:08.263727+08:00
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        def is_peak(index):
            if index == 0 and nums[index] > nums[index + 1]:
                return True
            if index == len(nums) - 1 and nums[index - 1] < nums[index]:
                return True
            if nums[index - 1] < nums[index] > nums[index + 1]:
                return True

        if len(nums) == 2:
            if is_peak(0):
                return 0
            if is_peak(1):
                return 1
        left, right = 0, len(nums) - 1
        while True:
            mid = (left + right) // 2
            if is_peak(mid):
                return mid
            if is_peak(left):
                return left
            if is_peak(right):
                return right

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            if nums[mid] < nums[mid - 1]:
                right = mid - 1


tests = [
    (
        ([1, 2, 3, 1],
         ),
        2,
    ),
    (
        ([1, 2, 1, 3, 5, 6, 4],
         ),
        5,
    ),
    (
        ([2, 1],
         ),
        0,
    ),
]


def validator(findPeakElement, inputs, expected):
    nums = inputs[0]
    output = findPeakElement(nums)

    def is_peak(index):
        if index == 0 and nums[index] > nums[index + 1]:
            return True
        if index == len(nums) - 1 and nums[index - 1] < nums[index]:
            return True
        if nums[index - 1] < nums[index] > nums[index + 1]:
            return True

    assert is_peak(output), (output, expected)
