"""
Problem:
    344. Reverse String
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/reverse-string
Tags:
    Two Pointers, String, Recursion
Date:
    2022-05-10T14:04:45.938890+08:00
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s) // 2):
            s[index], s[len(s) - index - 1] = s[len(s) - index - 1], s[index]


tests = [
    (
        (["h", "e", "l", "l", "o"],),
        ["o", "l", "l", "e", "h"],
    ),
    (
        (["H", "a", "n", "n", "a", "h"],),
        ["h", "a", "n", "n", "a", "H"],
    ),
]


def validator(reverseString, inputs, expected):
    s = inputs[0]
    reverseString(s)
    assert s == expected, (s, expected)
