"""
Problem:
    167. Two Sum II - Input Array Is Sorted
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
Tags:
    Array, Two Pointers, Binary Search
Date:
    2022-05-10T14:34:27.884808+08:00
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if target == two_sum:
                return [left + 1, right + 1]
            if target < two_sum:
                right -= 1
            if two_sum < target:
                left += 1


tests = [
    (
        ([2, 7, 11, 15], 9,
         ),
        [1, 2],
    ),
    (
        ([2, 3, 4], 6,
         ),
        [1, 3],
    ),
    (
        ([-1, 0], -1,
         ),
        [1, 2],
    ),
]
