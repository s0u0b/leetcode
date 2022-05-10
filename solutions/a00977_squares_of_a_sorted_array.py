"""
Problem:
    977. Squares of a Sorted Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/squares-of-a-sorted-array
Tags:
    Array, Two Pointers, Sorting
Date:
    2022-05-10T14:08:45.124496+08:00
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        squares_of_sorted = []
        while left <= right:
            left_num = nums[left] ** 2
            right_num = nums[right] ** 2
            if left_num < right_num:
                squares_of_sorted.insert(0, right_num)
                right -= 1
            else:
                squares_of_sorted.insert(0, left_num)
                left += 1
        return squares_of_sorted


tests = [
    (
        ([-4, -1, 0, 3, 10],
         ),
        [0, 1, 9, 16, 100],
    ),
    (
        ([-7, -3, 2, 3, 11],
         ),
        [4, 9, 9, 49, 121],
    ),
]
