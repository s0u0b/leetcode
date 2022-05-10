"""
Problem:
    1374. Generate a String With Characters That Have Odd Counts
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts
Tags:
    String
Date:
    2022-05-10T17:35:17.576933+08:00
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return (n - 1) * 'a' + 'b'
        else:
            return n * 'a'


tests = [
    (
        (4,
         ),
        "pppz",
    ),
    (
        (2,
         ),
        "xy",
    ),
    (
        (7,
         ),
        "holasss",
    ),
]


def validator(generateTheString, inputs, expected):
    n = inputs[0]
    output = generateTheString(n)
    output_len = len(output)
    output_list = list(output)
    output_str_set = set(output_list)
    count_of_c = 0
    for c in output_str_set:
        if output_list.count(c) % 2 == 0:
            count_of_c = 1
            break
    output = [output_len, count_of_c]
    expected = [n, 0]
    assert output == expected, (output, expected)
