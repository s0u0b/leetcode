"""
Problem:
    1346. Check If N and Its Double Exist
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/check-if-n-and-its-double-exist
Tags:
    Array, Hash Table, Two Pointers, Binary Search, Sorting
Date:
    2022-05-10T14:10:14.321033+08:00
"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, a in enumerate(arr):
            for j, b in enumerate(arr):
                if i != j:
                    if a * 2 == b:
                        return True
        return False


tests = [
    (
        ([10, 2, 5, 3],
         ),
        True,
    ),
    (
        ([7, 1, 14, 11],
         ),
        True,
    ),
    (
        ([3, 1, 7, 11],
         ),
        False,
    ),
]
