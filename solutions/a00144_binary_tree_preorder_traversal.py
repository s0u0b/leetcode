"""
Problem:
    144. Binary Tree Preorder Traversal
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/binary-tree-preorder-traversal
Tags:
    Stack, Tree, Depth-First Search, Binary Tree
Date:
    2022-05-10T14:03:02.807933+08:00
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def flat(node_list):
            flat_list = []
            for node in node_list:
                if isinstance(node, List):
                    node = [item for item in node]
                    flat_list += node
                elif node:
                    flat_list.append(node)
            return flat_list

        if root:
            node = [root.val, self.preorderTraversal(root.left), self.preorderTraversal(root.right)]
            return flat(node)
        else:
            return []


tests = [
    (
        ([1, None, 2, 3],
         ),
        [1, 2, 3],
    ),
    (
        ([],
         ),
        [],
    ),
    (
        ([1],
         ),
        [1],
    ),
]


def validator(preorderTraversal, inputs, expected):
    value = inputs[0]
    root = TreeNode.build_tree(value)
    output = preorderTraversal(root)
    assert output == expected, (output, expected)
