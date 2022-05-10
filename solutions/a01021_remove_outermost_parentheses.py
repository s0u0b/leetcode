"""
Problem:
    1021. Remove Outermost Parentheses
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/remove-outermost-parentheses
Tags:
    String, Stack
Date:
    2022-05-10T14:08:56.396615+08:00
"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        ans = ''
        for s in S:
            if s == '(':
                if stack:
                    ans += s
                stack.append(s)
            if s == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
                if stack:
                    ans += s
        return ans


tests = [
    (
        ("(()())(())",
         ),
        "()()()",
    ),
    (
        ("(()())(())(()(()))",
         ),
        "()()()()(())",
    ),
    (
        ("()()",
         ),
        "",
    ),
]
