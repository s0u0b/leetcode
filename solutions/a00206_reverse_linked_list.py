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
    2022-05-10T14:03:58.078126+08:00
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
        node_list = []
        dummy = ListNode()
        start = ListNode()
        dummy.next = start
        while head:
            node_list.append(head.val)
            head = head.next
        while node_list:
            start.next = ListNode(node_list.pop())
            start = start.next
        return dummy.next.next


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
