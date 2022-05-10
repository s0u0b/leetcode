"""
Problem:
    1684. Count the Number of Consistent Strings
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/count-the-number-of-consistent-strings
Tags:
    Array, Hash Table, String, Bit Manipulation
Date:
    2022-05-10T14:12:06.352159+08:00
"""
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        consistent = 0
        for word in words:
            if not set(word) - allowed:
                consistent += 1
        return consistent


tests = [
    (
        ("ab", ["ad", "bd", "aaab", "baa", "badab"],
         ),
        2,
    ),
    (
        ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"],
         ),
        7,
    ),
    (
        ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"],
         ),
        4,
    ),
]
