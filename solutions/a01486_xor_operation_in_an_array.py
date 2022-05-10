"""
Problem:
    1486. XOR Operation in an Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/xor-operation-in-an-array
Tags:
    Math, Bit Manipulation
Date:
    2022-05-10T14:11:22.578771+08:00
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        ans = 0
        for i, n in enumerate(nums):
            if i == 0:
                ans = n
            else:
                ans = ans ^ n
        return ans


tests = [
    (
        (5, 0,
         ),
        8,
    ),
    (
        (4, 3,
         ),
        8,
    ),
]
