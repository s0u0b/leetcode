"""
Problem:
    557. Reverse Words in a String III
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/reverse-words-in-a-string-iii
Tags:
    Two Pointers, String
Date:
    2022-05-10T14:06:21.358130+08:00
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split(' ')])


tests = [
    (
        ("Let's take LeetCode contest",
         ),
        "s'teL ekat edoCteeL tsetnoc",
    ),
    (
        ("God Ding",
         ),
        "doG gniD",
    ),
]
