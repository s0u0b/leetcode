"""
Problem:
    77. Combinations
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/combinations
Tags:
    Backtracking
Date:
    2022-05-10T14:02:39.730111+08:00
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num_list = [i for i in range(1, n + 1)]
        combine_list = []
        for i in range(2 ** n):
            binary_i = format(i, "b").rjust(n, '0')
            if binary_i.count('1') == k:
                combine_ = []
                for j, c in enumerate(binary_i):
                    if c == '1':
                        combine_.append(num_list[j])
                combine_list.append(combine_)
        return combine_list


tests = [
    (
        (4, 2,),
        [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
        ,
    ),
    (
        (1, 1,),
        [[1]],
    ),

]


def validator(combine, inputs, expected):
    n, k = inputs
    combine_list = combine(n, k)
    output = sorted(combine_list)
    expected = sorted(expected)
    assert output == expected, (output, expected)
