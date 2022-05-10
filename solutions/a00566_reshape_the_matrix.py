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
    2022-05-10T14:06:28.316717+08:00
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        reshape = []
        flat_mat = [element for row in mat for element in row]
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(flat_mat.pop(0))
            reshape.append(new_row)
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
