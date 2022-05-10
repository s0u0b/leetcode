"""
Problem:
    1342. Number of Steps to Reduce a Number to Zero
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero
Tags:
    Math, Bit Manipulation
Date:
    2022-05-10T14:10:10.888893+08:00
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            steps = steps + 1
            if num == 1:
                break
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
        return steps


tests = [
    (
        (14,
         ),
        6,
    ),
    (
        (8,
         ),
        4,
    ),
    (
        (123,
         ),
        12,
    ),
]
