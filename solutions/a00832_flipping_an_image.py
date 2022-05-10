"""
Problem:
    832. Flipping an Image
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/flipping-an-image
Tags:
    Array, Two Pointers, Matrix, Simulation
Date:
    2022-05-10T14:08:11.759578+08:00
"""
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for row in A:
            new_row = []
            for element in reversed(row):
                if element:
                    new_row.append(0)
                else:
                    new_row.append(1)
            ans.append(new_row)
        return ans


tests = [
    (
        ([[1, 1, 0], [1, 0, 1], [0, 0, 0]],
         ),
        [[1, 0, 0], [0, 1, 0], [1, 1, 1]],
    ),
    (
        ([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
         ),
        [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
    ),
]
