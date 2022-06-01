"""
Problem:
    1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers
Tags:
    String, Greedy
Date:
    2022-06-01T15:43:48.500028+08:00
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


tests = [
    (
        ("32",
         ),
        3,
    ),
    (
        ("82734",
         ),
        8,
    ),
    (
        ("27346209830709182346",
         ),
        9,
    ),
]
