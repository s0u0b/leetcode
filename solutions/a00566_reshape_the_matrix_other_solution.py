"""
Problem:
    566. Reshape the Matrix
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/reshape-the-matrix
Tags:
    Array, Matrix, Simulation
Date:
    2022-05-10T14:07:08.421813+08:00
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        if (m, n) == (r, c):
            return mat
        reshape = [[-1 for _ in range(c)] for _ in range(r)]

        for i in range(m):
            for j in range(n):
                if r >= 2 or m == 1 or n == 1:
                    reshape[(i * n + j) // c][(i * n + j) % c] = mat[i][j]
                else:
                    reshape[(i * n + j) % r][(i * n + j) % c] = mat[i][j]
        return reshape


tests = [
    (
        ([[1, 2], [3, 4]], 1, 4,
         ),
        [[1, 2, 3, 4]],
    ),
    (
        ([[1, 2], [3, 4]], 2, 4,
         ),
        [[1, 2], [3, 4]],
    ),
]
