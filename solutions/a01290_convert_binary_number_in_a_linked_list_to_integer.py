"""
Problem:
    1290. Convert Binary Number in a Linked List to Integer
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
Tags:
    Linked List, Math
Date:
    2022-05-10T14:09:44.677969+08:00
"""
from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys

sys.path.append('..')
from utils.list.list_node import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans


tests = [
    (
        ([1, 0, 1],
         ),
        5,
    ),
    (
        ([0],
         ),
        0,
    ),
]


def validator(getDecimalValue, inputs, expected):
    value = inputs[0]
    node = ListNode.list_to_list_node(value)
    output = getDecimalValue(node)
    assert output == expected, (output, expected)
