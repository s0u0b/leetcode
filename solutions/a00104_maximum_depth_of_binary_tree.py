"""
Problem:
    104. Maximum Depth of Binary Tree
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/maximum-depth-of-binary-tree
Tags:
    Tree, Depth-First Search, Breadth-First Search, Binary Tree
Date:
    2022-05-10T14:02:47.706812+08:00
"""
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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


tests = [
    (
        ([3, 9, 20, None, None, 15, 7],
         ),
        3,
    ),
    (
        ([1, None, 2],
         ),
        2,
    ),
]


def validator(maxDepth, inputs, expected):
    value = inputs[0]
    node = TreeNode.build_tree(value)
    output = maxDepth(node)
    assert output == expected, (output, expected)
