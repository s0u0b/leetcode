"""
Problem:
    1678. Goal Parser Interpretation
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/goal-parser-interpretation
Tags:
    String
Date:
    2022-05-10T14:12:03.489158+08:00
"""


class Solution:
    def interpret(self, command: str) -> str:
        goal_parser = command
        goal_parser = goal_parser.replace('()', 'o')
        goal_parser = goal_parser.replace('(', '')
        goal_parser = goal_parser.replace(')', '')
        return goal_parser


tests = [
    (
        ("G()(al)",
         ),
        "Goal",
    ),
    (
        ("G()()()()(al)",
         ),
        "Gooooal",
    ),
    (
        ("(al)G(al)()()G",
         ),
        "alGalooG",
    ),
]
