"""
Problem:
    1380. Lucky Numbers in a Matrix
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/lucky-numbers-in-a-matrix
Tags:
    Array, Matrix
Date:
    2022-05-10T14:10:33.534364+08:00
"""
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []
        tmp = []
        tmp_matrix = []
        for j in range(len(matrix[0])):
            tmp = []
            for i, m in enumerate(matrix):
                tmp.append(m[j])
            tmp_matrix.append(tmp)
        for i, m in enumerate(matrix):
            for j, e in enumerate(m):
                if e == min(matrix[i]) == max(tmp_matrix[j]):
                    lucky_numbers.append(e)
        return lucky_numbers


tests = [
    (
        ([[3, 7, 8], [9, 11, 13], [15, 16, 17]],
         ),
        [15],
    ),
    (
        ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]],
         ),
        [12],
    ),
    (
        ([[7, 8], [1, 2]],
         ),
        [7],
    ),
]
