"""
Problem:
    200. Number of Islands
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/number-of-islands
Tags:
    Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
Date:
    2022-05-10T14:03:11.198846+08:00
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        def walk_on_island(mark, pos):
            row, col = pos
            if row + 1 < row_len and grid[row + 1][col] == '1':
                grid[row + 1][col] = mark
                walk_on_island(mark, [row + 1, col])
            if row > 0 and grid[row - 1][col] == '1':
                grid[row - 1][col] = mark
                walk_on_island(mark, [row - 1, col])
            if col + 1 < col_len and grid[row][col + 1] == '1':
                grid[row][col + 1] = mark
                walk_on_island(mark, [row, col + 1])
            if col > 0 and grid[row][col - 1] == '1':
                grid[row][col - 1] = mark
                walk_on_island(mark, [row, col - 1])

        island_num = 0
        for row_index in range(row_len):
            for col_index in range(col_len):
                if grid[row_index][col_index] == '1':
                    island_num += 1
                    walk_on_island(island_num, [row_index, col_index])
        return island_num


tests = [
    (
        ([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],
         ),
        1,
    ),
    (
        ([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]],
         ),
        3,
    ),
]
