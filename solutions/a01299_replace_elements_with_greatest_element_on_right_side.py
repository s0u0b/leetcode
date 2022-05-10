"""
Problem:
    1299. Replace Elements with Greatest Element on Right Side
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side
Tags:
    Array
Date:
    2022-05-10T14:09:51.510409+08:00
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        for a in reversed(arr):
            if len(ans) == len(arr):
                break
            if a > ans[0]:
                ans = [a] + ans
            else:
                ans = [ans[0]] + ans
        return ans


tests = [
    (
        ([17, 18, 5, 4, 6, 1],
         ),
        [18, 6, 6, 6, 1, -1],
    ),
    (
        ([400],
         ),
        [-1],
    ),
]
