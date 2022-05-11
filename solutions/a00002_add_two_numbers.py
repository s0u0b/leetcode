"""
Problem:
    2. Add Two Numbers
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/add-two-numbers
Tags:
    Linked List, Math, Recursion
Date:
    2022-05-11T23:40:23.785141+08:00
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = ListNode()
        dummy.next = head
        carry = 0
        while l1 or l2:
            head.next = ListNode()
            head = head.next
            if l1.next and not l2.next:
                fake_node = ListNode()
                fake_node.val = 0
                l2.next = fake_node
            if l2.next and not l1.next:
                fake_node = ListNode()
                fake_node.val = 0
                l1.next = fake_node

            head.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next

        if carry:
            head.next = ListNode()
            head = head.next
            head.val = carry
        return dummy.next.next


tests = [
    (
        ([2, 4, 3], [5, 6, 4],
         ),
        [7, 0, 8],
    ),
    (
        ([0], [0],
         ),
        [0],
    ),
    (
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9],
         ),
        [8, 9, 9, 9, 0, 0, 0, 1],
    ),
]


def validator(addTwoNumbers, inputs, expected):
    l1, l2, = inputs
    l1, l2 = ListNode.list_to_list_node(l1), ListNode.list_to_list_node(l2)
    output = addTwoNumbers(l1, l2)
    output = ListNode.list_node_to_string(output)
    expected = ListNode.list_to_list_node_string(expected)
    assert output == expected, (output, expected)
