"""
Problem:
    542. 01 Matrix
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/01-matrix
Tags:
    Array, Dynamic Programming, Breadth-First Search, Matrix
Date:
    2022-05-10T14:06:15.543098+08:00
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        flag_matrix = [[True for _ in range(n)] for _ in range(m)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pos_list = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    pos_list.append([i, j])
                    flag_matrix[i][j] = False

        while pos_list:
            i, j = pos_list.pop(0)
            for direction in directions:
                dir_i, dir_j = direction
                new_i, new_j = i + dir_i, j + dir_j
                if 0 <= new_i < m and 0 <= new_j < n and flag_matrix[new_i][new_j]:
                    pos_list.append([new_i, new_j])
                    flag_matrix[new_i][new_j] = False
                    mat[new_i][new_j] = mat[i][j] + 1
        return mat


tests = [
    (
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]],
         ),
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    ),
    (
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]],
         ),
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
    ),
]
