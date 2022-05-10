"""
Problem:
    1252. Cells with Odd Values in a Matrix
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/cells-with-odd-values-in-a-matrix
Tags:
    Array, Math, Simulation
Date:
    2022-05-10T14:09:33.000936+08:00
"""
from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        column, row = n, m
        matrix = [[0] * row for _ in range(column)]
        ans = 0
        for pos in indices:
            x = pos[0]
            y = pos[1]
            for i, line in enumerate(matrix):
                for j, element in enumerate(line):
                    if i == x:
                        matrix[i][j] += 1
                    if j == y:
                        matrix[i][j] += 1
        for line in matrix:
            for element in line:
                if element % 2 == 1:
                    ans += 1
        return ans


tests = [
    (
        (2, 3, [[0, 1], [1, 1]],
         ),
        6,
    ),
    (
        (2, 2, [[1, 1], [0, 0]],
         ),
        0,
    ),
]
