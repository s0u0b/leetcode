"""
Problem:
    942. DI String Match
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/di-string-match
Tags:
    Array, Math, Two Pointers, String, Greedy
Date:
    2022-05-10T14:08:30.115848+08:00
"""
from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        nums = [x for x in range(len(S) + 1)]
        S = list(S)
        ans = []
        for s in S:
            if s == 'I':
                ans.append(nums.pop(0))
                pass
            else:
                ans.append(nums.pop())
                pass
        ans.append(nums.pop())
        return ans


tests = [
    (
        ("IDID",
         ),
        [0, 4, 1, 3, 2],
    ),
    (
        ("III",
         ),
        [0, 1, 2, 3],
    ),
    (
        ("DDI",
         ),
        [3, 2, 0, 1],
    ),
]
