"""
Problem:
    169. Majority Element
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/majority-element
Tags:
    Array, Hash Table, Divide and Conquer, Sorting, Counting
Date:
    2022-05-12T01:01:45.465500+08:00
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        element_count = {}
        for num in nums:
            if num not in element_count.keys():
                element_count[num] = 1
            else:
                element_count[num] += 1
            if element_count[num] > majority_count:
                return num


tests = [
    (
        ([3, 2, 3],
         ),
        3,
    ),
    (
        ([2, 2, 1, 1, 1, 2, 2],
         ),
        2,
    ),
]
