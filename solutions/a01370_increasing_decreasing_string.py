"""
Problem:
    1370. Increasing Decreasing String
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/increasing-decreasing-string
Tags:
    Hash Table, String, Counting
Date:
    2022-05-10T14:10:26.333928+08:00
"""


class Solution:
    def sortString(self, s: str) -> str:
        ans = ''
        s = list(s)
        increase = 1
        while s:
            if increase:
                s.sort()
                increase = 0

            else:
                s.sort(reverse=True)
                increase = 1

            tmp = ''
            tmp_list = []
            for c in s:
                if tmp != c:
                    ans = ans + c
                    tmp = c
                    tmp_list.append(c)
            for c in tmp_list:
                s.remove(c)
        return ans


tests = [
    (
        ("aaaabbbbcccc",
         ),
        "abccbaabccba",
    ),
    (
        ("rat",
         ),
        "art",
    ),
]
