"""
Problem:
    1304. Find N Unique Integers Sum up to Zero
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero
Tags:
    Array, Math
Date:
    2022-05-10T16:18:07.210680+08:00
"""
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)
        if n % 2:
            ans.append(0)
        return ans


tests = [
    (
        (5,
         ),
        [-7, -1, 1, 3, 4],
    ),
    (
        (3,
         ),
        [-1, 0, 1],
    ),
    (
        (1,
         ),
        [0],
    ),
]


def validator(sumZero, inputs, expected):
    n = inputs[0]
    output = sumZero(n)
    sum_of_output = sum(output)
    count_of_output = len(set(output))
    output = [sum_of_output, count_of_output]
    expected = [0, n]
    assert output == expected, (output, expected)
