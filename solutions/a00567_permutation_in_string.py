"""
Problem:
    567. Permutation in String
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/permutation-in-string
Tags:
    Hash Table, Two Pointers, String, Sliding Window
Date:
    2022-05-10T14:07:18.067614+08:00
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = 'abcdefghijklmnopqrstuvwxyz'
        s1_char_count, s2_char_count = dict.fromkeys(s, 0), dict.fromkeys(s, 0)
        s1_list, s2_list = list(s1), list(s2)
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False
        for c in set(s1):
            s1_char_count[c] = s1_list.count(c)
        for i in range(s1_len):
            s2_char_count[s2[i]] = s2_list[:s1_len].count(s2[i])
        if s1_char_count == s2_char_count:
            return True
        for i in range(s1_len, s2_len):
            s2_char_count[s2_list[i]] += 1
            s2_char_count[s2_list[i - s1_len]] -= 1
            if s1_char_count == s2_char_count:
                return True
        return False


tests = [
    (
        ("ab", "eidbaooo",
         ),
        True,
    ),
    (
        ("ab", "eidboaoo",
         ),
        False,
    ),
]
