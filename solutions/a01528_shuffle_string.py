"""
Problem:
    1528. Shuffle String
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/shuffle-string
Tags:
    Array, String
Date:
    2022-05-10T14:11:39.888884+08:00
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ''
        for i, element in enumerate(indices):
            ans += s[indices.index(i)]
        return ans


tests = [
    (
        ("codeleet", [4, 5, 6, 7, 0, 2, 1, 3],
         ),
        "leetcode",
    ),
    (
        ("abc", [0, 1, 2],
         ),
        "abc",
    ),
]
