"""
Problem:
    617. Merge Two Binary Trees
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/merge-two-binary-trees
Tags:
    Tree, Depth-First Search, Breadth-First Search, Binary Tree
Date:
    2022-05-10T14:07:22.884880+08:00
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
import sys

sys.path.append('..')
from utils.tree.tree_node import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if root1 and root2:
            root1.val += root2.val
            if root1.left:
                self.mergeTrees(root1.left, root2.left)
            else:
                root1.left = root2.left
            if root1.right:
                self.mergeTrees(root1.right, root2.right)
            else:
                root1.right = root2.right
        return root1


tests = [
    (
        ([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7],
         ),
        [3, 4, 5, 5, 4, None, 7],
    ),
    (
        ([1], [1, 2],
         ),
        [2, 2],
    ),
]


def validator(mergeTrees, inputs, expected):
    value1, value2 = inputs
    tree1, tree2 = TreeNode.build_tree(value1), TreeNode.build_tree(value2)
    output = mergeTrees(tree1, tree2)
    output = TreeNode.tree_to_list(output)
    assert output == expected, (output, expected)
