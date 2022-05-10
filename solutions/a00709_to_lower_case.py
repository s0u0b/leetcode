"""
Problem:
    709. To Lower Case
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/to-lower-case
Tags:
    String
Date:
    2022-05-10T14:07:46.501671+08:00
"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


tests = [
    (
        ("Hello",
         ),
        "hello",
    ),
    (
        ("here",
         ),
        "here",
    ),
    (
        ("LOVELY",
         ),
        "lovely",
    ),
]
