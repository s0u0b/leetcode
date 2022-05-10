"""
Problem:
    19. Remove Nth Node From End of List
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/remove-nth-node-from-end-of-list
Tags:
    Linked List, Two Pointers
Date:
    2022-05-10T14:00:29.877163+08:00
"""
from typing import List, Optional
import sys
sys.path.append('..')
from utils.list.list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        slow = fast = head
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        if head == slow and not fast:
            return head.next
        slow.next = slow.next.next

        return dummy_node.next


tests = [
    (
        ([1, 2, 3, 4, 5], 2,),
        [1, 2, 3, 5],
    ),
    (
        ([1], 1,),
        [],
    ),
    (
        ([1, 2], 1,),
        [1],
    ),
    (
        ([1, 2], 2,),
        [2],
    ),
]


def validator(removeNthFromEnd, inputs, expected):
    head, n = inputs
    head = ListNode.list_to_list_node(head)
    output = removeNthFromEnd(head, n)
    output = ListNode.list_node_to_string(output)
    expected = ListNode.list_to_list_node(expected)
    expected = ListNode.list_node_to_string(expected)
    assert output == expected, (output, expected)
