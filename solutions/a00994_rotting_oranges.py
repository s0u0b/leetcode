"""
Problem:
    994. Rotting Oranges
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/rotting-oranges
Tags:
    Array, Breadth-First Search, Matrix
Date:
    2022-05-10T14:08:48.197073+08:00
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten_positions = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_positions.append([i, j, 0])
        max_step = 0
        while rotten_positions:
            rotten_i, rotten_j, step = rotten_positions.pop(0)
            if grid[rotten_i][rotten_j] == 0:
                continue
            for direction in directions:
                direction_i, direction_j = direction
                new_i, new_j = rotten_i + direction_i, rotten_j + direction_j
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 2
                    rotten_positions.append([new_i, new_j, step + 1])
                    max_step = max(max_step, step + 1)
        for row in grid:
            if 1 in row:
                return -1
        return max_step


tests = [
    (
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]],
         ),
        4,
    ),
    (
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]],
         ),
        -1,
    ),
    (
        ([[0, 2]],
         ),
        0,
    ),
]
