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
    2022-05-10T14:05:17.403848+08:00
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        direction = -1
        pos_i, pos_j = direction * -1, direction
        diagonal_order = []
        while True:
            pos_i, pos_j = pos_i + direction, pos_j + direction * -1
            if 0 <= pos_i < m and 0 <= pos_j < n:
                diagonal_order.append(mat[pos_i][pos_j])
                if pos_i == m - 1 and pos_j == n - 1:
                    break
            elif pos_i < 0 and pos_j < n or pos_i >= m:
                direction *= -1
                pos_j += 1
            elif pos_j < 0 and pos_i < m or pos_j >= n:
                direction *= -1
                pos_i += 1
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
