"""
Problem:
    136. Single Number
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/single-number
Tags:
    Array, Bit Manipulation
Date:
    2022-05-12T00:57:29.075234+08:00
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = []
        for num in nums:
            if num in numbers:
                numbers.remove(num)
            else:
                numbers.append(num)
        return numbers[0]


tests = [
    (
        ([2, 2, 1],
         ),
        1,
    ),
    (
        ([4, 1, 2, 1, 2],
         ),
        4,
    ),
    (
        ([1],
         ),
        1,
    ),
]
