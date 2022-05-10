"""
Problem:
    46. Permutations
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/permutations
Tags:
    Array, Backtracking
Date:
    2022-05-10T14:00:29.877163+08:00
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation_list = []

        def directed_permutations(num1, i=0):
            if i == len(num1) - 1:
                permutation_list.append(num1)
            else:
                for j in range(i, len(num1)):
                    num2 = num1[:]
                    num2[i], num2[j] = num2[j], num2[i]
                    directed_permutations(num2, i + 1)

        directed_permutations(nums)
        return permutation_list


tests = [
    (
        ([1, 2, 3],
         ),
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
    ),
    (
        ([0, 1],
         ),
        [[0, 1], [1, 0]],
    ),
    (
        ([1],
         ),
        [[1]],
    ),
]


def validator(permute, inputs, expected):
    value = inputs[0]
    output = sorted(permute(value))
    expected = sorted(expected)
    assert output == expected, (output, expected)
