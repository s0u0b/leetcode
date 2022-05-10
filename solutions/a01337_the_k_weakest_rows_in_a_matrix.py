"""
Problem:
    1337. The K Weakest Rows in a Matrix
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix
Tags:
    Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
Date:
    2022-05-10T14:10:06.045636+08:00
"""
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = [[i, m.count(1)] for i, m in enumerate(mat)]
        counts = sorted(counts, key=lambda count: count[1])
        rows = []
        for row in counts[:k]:
            rows.append(row[0])
        return rows


tests = [
    (
        ([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3,
         ),
        [2, 0, 3],
    ),
    (
        ([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2,
         ),
        [0, 2],
    ),
]
