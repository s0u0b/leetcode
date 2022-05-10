"""
Problem:
    1089. Duplicate Zeros
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/duplicate-zeros
Tags:
    Array, Two Pointers
Date:
    2022-05-10T14:09:03.456922+08:00
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        find_zero = 1
        for i, a in enumerate(arr):
            if a == 0 and find_zero:
                find_zero = 0
                for n in range(len(arr) - 1, i, -1):
                    arr[n] = arr[n - 1]
            else:
                find_zero = 1


tests = [
    (
        ([1, 0, 2, 3, 0, 4, 5, 0],
         ),
        [1, 0, 0, 2, 3, 0, 0, 4],
    ),
    (
        ([1, 2, 3],
         ),
        [1, 2, 3],
    ),
]


def validator(duplicateZeros, inputs, expected):
    output = inputs[0]
    duplicateZeros(output)
    assert output == expected, (output, expected)
