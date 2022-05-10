"""
Problem:
    36. Valid Sudoku
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/valid-sudoku
Tags:
    Array, Hash Table, Matrix
Date:
    2022-05-10T14:00:29.877163+08:00
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_board = [[] for _ in range(9)]
        sub_box_board = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                col_board[i].append(board[j][i])
                sub_box_board[i // 3 * 3 + j // 3].append(board[i][j])
        for i in range(9):
            for j in range(1, 10):
                if board[i].count(str(j)) > 1:
                    return False
                if col_board[i].count(str(j)) > 1:
                    return False
                if sub_box_board[i].count(str(j)) > 1:
                    return False
        return True


tests = [
    (
        ([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
         ),
        True,
    ),
    (
        ([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
         ),
        False,
    ),
]
