"""
Problem:
    206. Reverse Linked List
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/reverse-linked-list
Tags:
    Linked List, Recursion
Date:
    2022-05-10T14:04:12.871646+08:00
"""
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys

sys.path.append('..')
from utils.list.list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            temp_node = current.next
            current.next = previous
            previous = current
            current = temp_node
        return previous


tests = [
    (
        ([1, 2, 3, 4, 5],),
        [5, 4, 3, 2, 1],
    ),
    (
        ([],),
        [],
    ),

]


def validator(reverseList, inputs, expected):
    value = inputs[0]
    node = ListNode.list_to_list_node(value)
    output = ListNode.list_node_to_string(reverseList(node))
    expected = ListNode.list_to_list_node_string(expected)
    assert output == expected, (output, expected)
