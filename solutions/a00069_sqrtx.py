"""
Problem:
    69. Sqrt(x)
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/sqrtx
Tags:
    Math, Binary Search
Date:
    2022-05-10T14:02:31.117135+08:00
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x // 2
        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2
            next_square = (mid + 1) ** 2
            if square <= x < next_square:
                return mid
            if x < square:
                right = mid - 1
            if square < x:
                left = mid + 1
        else:
            return left


tests = [
    (
        (4,
         ),
        2,
    ),
    (
        (8,
         ),
        2,
    ),
]
