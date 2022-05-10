"""
Problem:
    876. Middle of the Linked List
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/middle-of-the-linked-list
Tags:
    Linked List, Two Pointers
Date:
    2022-05-10T14:08:20.270786+08:00
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


tests = [
    (
        ([1, 2, 3, 4, 5],
         ),
        [3, 4, 5],
    ),
    (
        ([1, 2, 3, 4, 5, 6],
         ),
        [4, 5, 6],
    ),
]


def validator(middleNode, inputs, expected):
    node_value = inputs[0]
    list_node = ListNode.list_to_list_node(node_value)
    output = middleNode(list_node)
    output = ListNode.list_node_to_string(output)
    expected = ListNode.list_to_list_node(expected)
    expected = ListNode.list_node_to_string(expected)
    assert output == expected, (output, expected)
