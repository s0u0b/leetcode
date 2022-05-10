"""
Problem:
    1295. Find Numbers with Even Number of Digits
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/find-numbers-with-even-number-of-digits
Tags:
    Array
Date:
    2022-05-10T14:09:48.329753+08:00
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        list_n = [str(x) for x in nums]
        for n in list_n:
            if len(n) % 2 == 0:
                ans = ans + 1
        return ans


tests = [
    (
        ([12, 345, 2, 6, 7896],
         ),
        2,
    ),
    (
        ([555, 901, 482, 1771],
         ),
        1,
    ),
]
