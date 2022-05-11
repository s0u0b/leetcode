"""
Problem:
    28. Implement strStr()
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/implement-strstr
Tags:
    Two Pointers, String, String Matching
Date:
    2022-05-11T18:48:30.341523+08:00
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1


tests = [
    (
        ("hello", "ll",
         ),
        2,
    ),
    (
        ("aaaaa", "bba",
         ),
        -1,
    ),
]
