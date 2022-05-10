"""
Problem:
    59. Spiral Matrix II
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/spiral-matrix-ii
Tags:
    Array, Matrix, Simulation
Date:
    2022-05-10T14:02:27.441888+08:00
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        def rotate(direction) -> List[int]:
            x, y = direction
            if not y:
                x *= -1
            return [y, x]

        def reverse(direction) -> List[int]:
            x, y = direction
            return [x * -1, y * -1]

        mid = n // 2
        new_matrix = [
            [True if x + y == n - 1 or x == y and x >= y >= mid or x - 1 == y and y <= x <= mid else False for y in
             range(n)] for x in range(n)]

        def go_next(pos: List[int], direction: List[int]):
            (x_pos, y_pos), (x_reverse, y_reverse) = pos, reverse(direction)
            (x_direction, y_direction) = rotate(direction) if new_matrix[x_pos][y_pos] else direction
            if isinstance(new_matrix[x_pos][y_pos], bool):
                new_matrix[x_pos][y_pos] = new_matrix[x_pos + x_reverse][y_pos + y_reverse] + 1
                go_next([x_pos + x_direction, y_pos + y_direction], [x_direction, y_direction])

        new_matrix[0][0] = 1
        first_step = initial_direction = [0, 1]
        go_next(first_step, initial_direction)
        return new_matrix


tests = [
    (
        (3,
         ),
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
    ),
    (
        (1,
         ),
        [[1]],
    ),
]
