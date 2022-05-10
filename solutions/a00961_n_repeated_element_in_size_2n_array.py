"""
Problem:
    961. N-Repeated Element in Size 2N Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/n-repeated-element-in-size-2n-array
Tags:
    Array, Hash Table
Date:
    2022-05-10T14:08:42.304615+08:00
"""
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        while A:
            tmp = A[0]
            A.remove(tmp)
            if tmp in A:
                return tmp


tests = [
    (
        ([1, 2, 3, 3],
         ),
        3,
    ),
    (
        ([2, 1, 2, 5, 3, 2],
         ),
        2,
    ),
    (
        ([5, 1, 5, 2, 5, 3, 5, 4],
         ),
        5,
    ),
]
