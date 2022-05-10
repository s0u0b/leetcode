"""
Problem:
    1773. Count Items Matching a Rule
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/count-items-matching-a-rule
Tags:
    Array, String
Date:
    2022-05-10T14:12:18.900137+08:00
"""
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_list = ["type", "color", "name"]
        key_index = key_list.index(ruleKey)
        ans = 0
        for item in items:
            if ruleValue == item[key_index]:
                ans += 1
        return ans


tests = [
    (
        ([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], "color", "silver",
         ),
        1,
    ),
    (
        ([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type", "phone",
         ),
        2,
    ),
]
