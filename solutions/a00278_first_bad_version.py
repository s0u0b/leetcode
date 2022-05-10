"""
Problem:
    278. First Bad Version
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/first-bad-version
Tags:
    Binary Search, Interactive
Date:
    2022-05-10T14:04:36.896120+08:00
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        else:
            return left


tests = [
    (
        (5, 4,
         ),
        4,
    ),
    (
        (1, 1,
         ),
        1,
    ),
]


def isBadVersion(version: int) -> bool:
    if version >= target:
        return True
    return False


def validator(firstBadVersion, inputs, expected):
    global target
    target = expected
    n, nums = inputs
    output = firstBadVersion(n)
    assert output == expected, (output, expected)
