"""
Problem:
    784. Letter Case Permutation
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/letter-case-permutation
Tags:
    String, Backtracking, Bit Manipulation
Date:
    2022-05-10T14:08:03.270803+08:00
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        letter_index = []
        binary_list = []
        letter_case_permutation = []
        for i, c in enumerate(s):
            if c.islower():
                letter_index.append(i)
        for i in range(2 ** len(letter_index)):
            binary_list.append(format(i, 'b').rjust(len(letter_index), '0'))
        for binary in binary_list:
            new_s = list(s[:])
            for i, b in enumerate(binary):
                if b == '1':
                    new_s[letter_index[i]] = new_s[letter_index[i]].upper()
            letter_case_permutation.append(''.join(new_s))

        return letter_case_permutation


tests = [
    (
        ("a1b2",
         ),
        ["a1b2", "a1B2", "A1b2", "A1B2"],
    ),
    (
        ("3z4",
         ),
        ["3z4", "3Z4"],
    ),
]


def validator(letterCasePermutation, inputs, expected):
    s = inputs[0]
    output = letterCasePermutation(s)
    output = sorted(output)
    expected = sorted(expected)
    assert output == expected, (output, expected)
