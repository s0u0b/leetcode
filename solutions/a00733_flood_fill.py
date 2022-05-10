"""
Problem:
    733. Flood Fill
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/flood-fill
Tags:
    Array, Depth-First Search, Breadth-First Search, Matrix
Date:
    2022-05-10T14:07:52.825663+08:00
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row_length = len(image)
        col_length = len(image[0])

        def go_next(color, pos):
            row, col = pos
            if row + 1 < row_length and image[row + 1][col] == color:
                image[row + 1][col] = newColor
                go_next(color, [row + 1, col])
            if row > 0 and image[row - 1][col] == color:
                image[row - 1][col] = newColor
                go_next(color, [row - 1, col])
            if col + 1 < col_length and image[row][col + 1] == color:
                image[row][col + 1] = newColor
                go_next(color, [row, col + 1])
            if col > 0 and image[row][col - 1] == color:
                image[row][col - 1] = newColor
                go_next(color, [row, col - 1])

        if image[sr][sc] == newColor:
            return image
        go_next(image[sr][sc], [sr, sc])
        image[sr][sc] = newColor
        return image


tests = [
    (
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2,
         ),
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
    ),
    (
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 2,
         ),
        [[2, 2, 2], [2, 2, 2]],
    ),
]
