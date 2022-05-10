"""
Problem:
    1207. Unique Number of Occurrences
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/unique-number-of-occurrences
Tags:
    Array, Hash Table
Date:
    2022-05-10T14:09:16.348556+08:00
"""
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = dict()
        arr = [str(x) for x in arr]
        for a in arr:
            if dic.get(a):
                dic[a] = dic[a] + 1
            else:
                dic[a] = 1
        if len(set(dic.values())) == len(set(arr)):
            return True
        else:
            return False


tests = [
    (
        ([1, 2, 2, 1, 1, 3],
         ),
        True,
    ),
    (
        ([1, 2],
         ),
        False,
    ),
    (
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],
         ),
        True,
    ),
]
