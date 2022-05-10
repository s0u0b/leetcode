"""
Problem:
    102. Binary Tree Level Order Traversal
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/binary-tree-level-order-traversal
Tags:
    Tree, Breadth-First Search, Binary Tree
Date:
    2022-05-10T14:02:45.090909+08:00
"""
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

sys.path.append('..')
from utils.tree.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        def helper(node, level):
            if node:
                if len(levels) == level:
                    levels.append([])
                levels[level] += [node.val]
                helper(node.left, level + 1)
                helper(node.right, level + 1)

        helper(root, 0)
        return levels


tests = [
    (
        ([3, 9, 20, None, None, 15, 7],
         ),
        [[3], [9, 20], [15, 7]],
    ),
    (
        ([1],
         ),
        [[1]],
    ),
    (
        ([],
         ),
        [],
    ),
]


def validator(levelOrder, inputs, expected):
    value = inputs[0]
    tree = TreeNode.build_tree(value)
    output = levelOrder(tree)
    assert output == expected, (output, expected)
