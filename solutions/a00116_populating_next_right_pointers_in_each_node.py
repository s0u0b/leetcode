"""
Problem:
    116. Populating Next Right Pointers in Each Node
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node
Tags:
    Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
Date:
    2022-05-10T14:02:51.723416+08:00
"""
from typing import Optional
import sys

sys.path.append('..')
from utils.tree.tree_node import Node

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        levels = []

        def level_order(level_root, level):
            if level == len(levels):
                levels.append([])
            levels[level].append(level_root)
            if level_root.left:
                level_order(level_root.left, level + 1)
                level_order(level_root.right, level + 1)

        level_order(root, 0)
        for level in levels:
            for i, node in enumerate(level[:-1]):
                node.next = level[i + 1]

        return root


tests = [
    (
        ([1, 2, 3, 4, 5, 6, 7],),
        [1, None, 2, 3, None, 4, 5, 6, 7, None],
    ),
    (
        ([],),
        [],
    ),
]


def validator(connect, inputs, expected):
    value = inputs[0]
    tree = Node.build_tree(value)
    output = connect(tree)
    output = Node.node_to_list(output)
    assert output == expected, (output, expected)
