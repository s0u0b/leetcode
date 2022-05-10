"""
Problem:
    350. Intersection of Two Arrays II
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/intersection-of-two-arrays-ii
Tags:
    Array, Hash Table, Two Pointers, Binary Search, Sorting
Date:
    2022-05-10T14:04:47.987970+08:00
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        intersections = []
        for num in nums1:
            if num in nums2:
                intersections += [num]
                nums2.remove(num)
        return intersections


tests = [
    (
        ([1, 2, 2, 1], [2, 2],
         ),
        [2, 2],
    ),
    (
        ([4, 9, 5], [9, 4, 9, 8, 4],
         ),
        [4, 9],
    ),
]
