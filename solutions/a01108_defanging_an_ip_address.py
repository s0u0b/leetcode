"""
Problem:
    1108. Defanging an IP Address
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/defanging-an-ip-address
Tags:
    String
Date:
    2022-05-10T14:09:11.074404+08:00
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.', '[.]')
        return address


tests = [
    (
        ("1.1.1.1",
         ),
        "1[.]1[.]1[.]1",
    ),
    (
        ("255.100.50.0",
         ),
        "255[.]100[.]50[.]0",
    ),
]
