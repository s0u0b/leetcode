"""
Problem:
    21. Merge Two Sorted Lists
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/merge-two-sorted-lists
Tags:
    Linked List, Recursion
Date:
    2022-05-10T14:00:29.877163+08:00
"""
from typing import List, Optional
import sys

sys.path.append('..')
from utils.list.list_node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        dummy = ListNode()
        dummy.next = new_node
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    new_node.next = list1
                    list1 = list1.next
                else:
                    new_node.next = list2
                    list2 = list2.next
            elif list1:
                new_node.next = list1
                list1 = list1.next
            elif list2:
                new_node.next = list2
                list2 = list2.next
            new_node = new_node.next
        return dummy.next.next


tests = [
    (
        ([1,2,4], [1,3,4],
        ),
         [1,1,2,3,4,4],
    ),
    (
        ([], [],
        ),
         [],
    ),
    (
        ([], [0],
        ),
         [0],
    ),
]

def validator(mergeTwoLists, inputs, expected):
    list1, list2 = inputs
    list1, list2 = ListNode.list_to_list_node(list1), ListNode.list_to_list_node(list2)
    output = mergeTwoLists(list1, list2)
    output = ListNode.list_node_to_string(output)
    expected = ListNode.list_to_list_node_string(expected)
    assert output == expected, (output, expected)