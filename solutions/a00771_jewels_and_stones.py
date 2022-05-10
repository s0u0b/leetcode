"""
Problem:
    771. Jewels and Stones
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/jewels-and-stones
Tags:
    Hash Table, String
Date:
    2022-05-10T14:07:59.308757+08:00
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for x in S:
            if J.find(x) != -1:
                count = count + 1
        return count


tests = [
    (
        ("aA", "aAAbbbb",
         ),
        3,
    ),
    (
        ("z", "ZZ",
         ),
        0,
    ),
]
