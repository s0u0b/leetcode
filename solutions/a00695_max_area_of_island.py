"""
Problem:
    695. Max Area of Island
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/max-area-of-island
Tags:
    Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
Date:
    2022-05-10T14:07:39.005798+08:00
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        def go_next(pos):
            row, col = pos
            if grid[row][col] == 1:
                grid[row][col] = 0
                up = down = left = right = 0
                if row - 1 >= 0:
                    if grid[row - 1][col] == 1:
                        up += go_next([row - 1, col])
                if row + 1 <= row_len - 1:
                    if grid[row + 1][col] == 1:
                        down += go_next([row + 1, col])
                if col - 1 >= 0:
                    if grid[row][col - 1] == 1:
                        left += go_next([row, col - 1])
                if col + 1 <= col_len - 1:
                    if grid[row][col + 1] == 1:
                        right += go_next([row, col + 1])
                return 1 + sum([up, down, left, right])
            else:
                return 0

        max_ = 0
        for i in range(row_len):
            for j in range(col_len):
                max_ = max(max_, go_next([i, j]))
        return max_


tests = [
    (
        ([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],
         ),
        6,
    ),
    (
        ([[0, 0, 0, 0, 0, 0, 0, 0]],
         ),
        0,
    ),
]
