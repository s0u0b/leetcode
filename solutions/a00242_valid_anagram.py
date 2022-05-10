"""
Problem:
    242. Valid Anagram
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/valid-anagram
Tags:
    Hash Table, String, Sorting
Date:
    2022-05-10T14:04:34.396088+08:00
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            s, t = t, s
        s_set = set(s)
        s_list = list(s)
        t_list = list(t)
        for c in s_set:
            if s_list.count(c) != t_list.count(c):
                return False
        else:
            return True


tests = [
    (
        ("anagram", "nagaram",
         ),
        True,
    ),
    (
        ("rat", "car",
         ),
        False,
    ),
]
