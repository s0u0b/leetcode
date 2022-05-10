"""
Problem:
    1572. Matrix Diagonal Sum
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/matrix-diagonal-sum
Tags:
    Array, Matrix
Date:
    2022-05-10T18:34:00.887209+08:00
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for i, ma in enumerate(mat):
            for j, m in enumerate(ma):
                if i == j or len(ma) - j - 1 == i:
                    ans += m
        return ans


tests = [
    (
        ([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]],
         ),
        25,
    ),
    (
        ([[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]],
         ),
        8,
    ),
    (
        ([[5]],
         ),
        5,
    ),
]
