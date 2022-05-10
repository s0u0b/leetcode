"""
Problem:
    118. Pascal's Triangle
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/pascals-triangle
Tags:
    Array, Dynamic Programming
Date:
    2022-05-10T14:02:55.880862+08:00
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(1, numRows):
            pascal.append([1])
            for j in range(i - 1):
                pascal[i].append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            pascal[i].append(1)
        return pascal


tests = [
    (
        (5,
         ),
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
    ),
    (
        (1,
         ),
        [[1]],
    ),
]
