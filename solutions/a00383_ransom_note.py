"""
Problem:
    383. Ransom Note
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/ransom-note
Tags:
    Hash Table, String, Counting
Date:
    2022-05-10T14:04:57.743608+08:00
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_set = set(ransomNote)
        ransom_note_list = list(ransomNote)
        magazine_list = list(magazine)
        for c in ransom_note_set:
            if ransom_note_list.count(c) > magazine_list.count(c):
                return False
        else:
            return True


tests = [
    (
        ("a", "b",
         ),
        False,
    ),
    (
        ("aa", "ab",
         ),
        False,
    ),
    (
        ("aa", "aab",
         ),
        True,
    ),
]
