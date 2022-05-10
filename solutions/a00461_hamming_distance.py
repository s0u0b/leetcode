"""
Problem:
    461. Hamming Distance
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/hamming-distance
Tags:
    Bit Manipulation
Date:
    2022-05-10T14:05:11.857182+08:00
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        x = list('{:032b}'.format(x))
        y = list('{:032b}'.format(y))
        for a, b in zip(x, y):
            if a != b:
                ans += 1
        return ans


tests = [
    (
        (1, 4,
         ),
        2,
    ),
    (
        (3, 1,
         ),
        1,
    ),
]
