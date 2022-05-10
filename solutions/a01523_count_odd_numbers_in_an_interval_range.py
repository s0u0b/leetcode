"""
Problem:
    1523. Count Odd Numbers in an Interval Range
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/count-odd-numbers-in-an-interval-range
Tags:
    Math
Date:
    2022-05-10T14:11:37.046928+08:00
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (low % 2 or high % 2)


tests = [
    (
        (3, 7,
         ),
        3,
    ),
    (
        (8, 10,
         ),
        1,
    ),
]
