"""
Problem:
    88. Merge Sorted Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/merge-sorted-array
Tags:
    Array, Two Pointers, Sorting
Date:
    2022-05-10T14:02:41.814787+08:00
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:])


tests = [
    (
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3,
         ),
        [1, 2, 2, 3, 5, 6],
    ),
    (
        ([1], 1, [], 0,
         ),
        [1],
    ),
    (
        ([0], 0, [1], 1,
         ),
        [1],
    ),
]


def validator(merge, inputs, expected):
    nums1, m, nums2, n = inputs
    merge(nums1, m, nums2, n)
    assert nums1 == expected, (nums1, expected)
