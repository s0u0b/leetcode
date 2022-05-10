"""
Problem:
    1221. Split a String in Balanced Strings
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/split-a-string-in-balanced-strings
Tags:
    String, Greedy, Counting
Date:
    2022-05-10T14:09:28.740674+08:00
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        a = s[0]
        balanced = 0
        for i in range(len(s)):
            if s[i] == a:
                balanced += 1
            else:
                balanced -= 1
            if balanced == 0:
                count += 1
        return count


tests = [
    (
        ("RLRRLLRLRL",
         ),
        4,
    ),
    (
        ("RLLLLRRRLR",
         ),
        3,
    ),
    (
        ("LLLLRRRR",
         ),
        1,
    ),
]
