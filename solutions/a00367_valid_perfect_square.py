"""
Problem:
    367. Valid Perfect Square
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/valid-perfect-square
Tags:
    Math, Binary Search
Date:
    2022-05-10T14:04:51.755908+08:00
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        last_digit = num % 10
        if last_digit not in [1, 4, 5, 6, 9, 0]:
            return False

        left, right = 1, num // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            square_number = mid ** 2
            if square_number == num:
                return True
            if num < square_number:
                right = mid - 1
            if square_number < num:
                left = mid + 1
        return False


tests = [
    (
        (16,
         ),
        True,
    ),
    (
        (14,
         ),
        False,
    ),
]
