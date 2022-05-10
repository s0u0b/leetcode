"""
Problem:
    1720. Decode XORed Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/decode-xored-array
Tags:
    Array, Bit Manipulation
Date:
    2022-05-10T14:12:11.991839+08:00
"""
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for code in encoded:
            ans.append(code ^ first)
            first = code ^ first
            pass
        return ans


tests = [
    (
        ([1, 2, 3], 1,
         ),
        [1, 0, 2, 1],
    ),
    (
        ([6, 2, 7, 3], 4,
         ),
        [4, 2, 0, 7, 4],
    ),
]
