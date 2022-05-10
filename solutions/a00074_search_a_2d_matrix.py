"""
Problem:
    74. Search a 2D Matrix
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/search-a-2d-matrix
Tags:
    Array, Binary Search, Matrix
Date:
    2022-05-10T14:02:35.126144+08:00
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            if target in matrix[0]:
                return True
            else:
                return False
        if n == 1:
            for element in matrix:
                if element[0] == target:
                    return True
            return False
        row_left, row_right = 0, m
        while row_left < row_right:
            mid = (row_left + row_right) // 2
            if matrix[mid][0] < target <= matrix[mid][-1]:
                row_left = mid
                break
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                row_left = mid + 1
            elif matrix[mid][0] > target:
                row_right = mid - 1

        row_index = row_left
        if row_index >= m:
            return False
        if target < matrix[row_index][0]:
            row_index -= 1
        if target > matrix[row_index][-1]:
            row_index += 1
        col_left, col_right = 0, n

        while col_left < col_right:
            mid = (col_left + col_right) // 2
            if matrix[row_index][mid] == target:
                return True
            if matrix[row_index][mid] < target:
                col_left = mid + 1
            if matrix[row_index][mid] > target:
                col_right = mid - 1
        if col_left >= n:
            return False
        if matrix[row_index][col_left] == target:
            return True
        return False


tests = [
    (
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3,
         ),
        True,
    ),
    (
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13,
         ),
        False,
    ),
]
