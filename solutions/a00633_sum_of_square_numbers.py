"""
Problem:
    633. Sum of Square Numbers
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/sum-of-square-numbers
Tags:
    Math, Two Pointers, Binary Search
Date:
    2022-05-10T14:07:26.963447+08:00
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square_list = []
        for i in range(int(c ** 0.5) + 1):
            square_list.append(i ** 2)
        for num1 in square_list:
            target = c - num1
            left, right = 0, len(square_list) - 1
            while left <= right:
                mid = (left + right) // 2
                if square_list[mid] == target:
                    return True
                if target < square_list[mid]:
                    right = mid - 1
                if square_list[mid] < target:
                    left = mid + 1
        return False


tests = [
    (
        (5,
         ),
        True,
    ),
    (
        (3,
         ),
        False,
    ),
]
