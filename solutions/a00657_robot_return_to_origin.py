"""
Problem:
    657. Robot Return to Origin
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/robot-return-to-origin
Tags:
    String, Simulation
Date:
    2022-05-10T14:07:33.167936+08:00
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = list(moves)
        mapp = {'U': 0, 'D': 0, 'R': 0, 'L': 0}
        for move in moves:
            mapp[move] = mapp[move] + 1
        if mapp['U'] == mapp['D'] and mapp['L'] == mapp['R']:
            return True
        else:
            return False


tests = [
    (
        ("UD",
         ),
        True,
    ),
    (
        ("LL",
         ),
        False,
    ),
]
