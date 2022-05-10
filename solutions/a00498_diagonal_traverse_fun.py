"""
Problem:
    498. Diagonal Traverse
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/diagonal-traverse
Tags:
    Array, Matrix, Simulation
Date:
    2022-05-10T14:06:00.820843+08:00
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def get_diagonal(diagonal_x, diagonal_y, matrix_len):
            diagonal_pos = []
            while diagonal_y >= 0 and diagonal_x < matrix_len:
                diagonal_pos.append([diagonal_x, diagonal_y])
                diagonal_x += 1
                diagonal_y -= 1
            return diagonal_pos

        m, n = len(mat), len(mat[0])
        diagonals = []
        diagonal_order = []
        for col in range(n):
            diagonals.append(get_diagonal(0, col, m))
        for row in range(1, m):
            diagonals.append(get_diagonal(row, n - 1, m))
        for i, diagonal in enumerate(diagonals):
            if not i % 2:
                diagonal.reverse()
            for pos in diagonal:
                x, y = pos
                diagonal_order.append(mat[x][y])
        return diagonal_order


tests = [
    (
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         ),
        [1, 2, 4, 7, 5, 3, 6, 8, 9],
    ),
    (
        ([[1, 2], [3, 4]],
         ),
        [1, 2, 3, 4],
    ),
]
