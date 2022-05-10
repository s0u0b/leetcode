"""
Problem:
    1309. Decrypt String from Alphabet to Integer Mapping
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping
Tags:
    String
Date:
    2022-05-10T14:09:57.863463+08:00
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ''
        count = 0
        tmp = ''
        for c in reversed(s):
            if c == '#':
                count = 2
                tmp = ''
                continue
            if count:
                count = count - 1
                tmp = c + tmp
            else:
                tmp = c
            if not count:
                ans = chr(int(tmp) + 96) + ans
        return ans


tests = [
    (
        ("10#11#12",
         ),
        "jkab",
    ),
    (
        ("1326#",
         ),
        "acz",
    ),
]
