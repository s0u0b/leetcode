"""
Problem:
    387. First Unique Character in a String
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/first-unique-character-in-a-string
Tags:
    Hash Table, String, Queue, Counting
Date:
    2022-05-10T14:05:00.759016+08:00
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        else:
            return -1


tests = [
    (
        ("leetcode",
         ),
        0,
    ),
    (
        ("loveleetcode",
         ),
        2,
    ),
    (
        ("aabb",
         ),
        -1,
    ),
]
