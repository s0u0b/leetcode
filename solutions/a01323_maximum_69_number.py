"""
Problem:
    1323. Maximum 69 Number
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/maximum-69-number
Tags:
    Math, Greedy
Date:
    2022-05-10T14:10:03.498852+08:00
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        ans = ''
        flag = 1
        for n in num:
            if n == '6' and flag:
                n = '9'
                flag = 0
            ans += n
        return int(ans)


tests = [
    (
        (9669,
         ),
        9969,
    ),
    (
        (9996,
         ),
        9999,
    ),
    (
        (9999,
         ),
        9999,
    ),
]
