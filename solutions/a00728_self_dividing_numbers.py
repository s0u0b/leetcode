"""
Problem:
    728. Self Dividing Numbers
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/self-dividing-numbers
Tags:
    Math
Date:
    2022-05-10T14:07:50.701432+08:00
"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            num_str = (list(str(num)))
            for digits in num_str:
                if int(digits) == 0:
                    break
                if num % int(digits):
                    break
            else:
                ans.append(num)
        return ans


tests = [
    (
        (1, 22,
         ),
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22],
    ),
    (
        (47, 85,
         ),
        [48, 55, 66, 77],
    ),
]
