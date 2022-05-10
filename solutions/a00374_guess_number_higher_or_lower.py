"""
Problem:
    374. Guess Number Higher or Lower
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/guess-number-higher-or-lower
Tags:
    Binary Search, Interactive
Date:
    2022-05-10T14:04:54.513697+08:00
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                right = mid - 1
            if guess(mid) == 1:
                left = mid + 1


tests = [
    (
        (10, 6,
         ),
        6,
    ),
    (
        (1, 1,
         ),
        1,
    ),
    (
        (2, 1,
         ),
        1,
    ),
]


def guess(num: int) -> int:
    if num > target:
        return -1
    if num < target:
        return 1
    return 0


def validator(guessNumber, inputs, expected):
    global target
    target = expected
    n, nums = inputs
    output = guessNumber(n)
    assert output == expected, (output, expected)
