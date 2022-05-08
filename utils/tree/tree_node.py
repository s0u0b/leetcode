from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        return f'TreeNode({self.val})'

    @classmethod
    def build_tree(cls, values: list[Optional[int]]):
        if len(values) == 0:
            return None

        if values[0] is None:
            return None

        root = TreeNode(values[0])
        queue: Deque[TreeNode] = deque()

        current_node = root
        children_assigned = 0
        for num in values[1:]:
            value = None if num is None else TreeNode(num)

            if children_assigned == 2:
                current_node = queue.popleft()
                children_assigned = 0

            if children_assigned == 0:
                current_node.left = value

            elif children_assigned == 1:
                current_node.right = value

            if value is not None:
                queue.append(value)

            children_assigned += 1

        return root

    @classmethod
    def tree_to_list(cls, root):
        levels = []

        def level_order(node, level):
            if len(levels) == level:
                levels.append([])
            if node:
                levels[level] += [node.val]
                level_order(node.left, level + 1)
                level_order(node.right, level + 1)
            else:
                levels[level] += [node]

        level_order(root, 0)

        def flat(node_list):
            flat_list = []
            for node in node_list:
                for element in node:
                    flat_list.append(element)

            while flat_list and flat_list[-1] is None:
                del flat_list[-1]
            return flat_list

        return flat(levels)


class Node(TreeNode):
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        super().__init__(val)
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @classmethod
    def build_tree(cls, values: list[Optional[int]]):
        if len(values) == 0:
            return None

        if values[0] is None:
            return None

        root = Node(values[0])
        queue: Deque[TreeNode] = deque()

        current_node = root
        children_assigned = 0
        for num in values[1:]:
            value = None if num is None else Node(num)

            if children_assigned == 2:
                current_node = queue.popleft()
                children_assigned = 0

            if children_assigned == 0:
                current_node.left = value

            elif children_assigned == 1:
                current_node.right = value

            if value is not None:
                queue.append(value)

            children_assigned += 1

        return root

    @classmethod
    def node_to_list(cls, node_root):
        levels = []

        def level_order(root, level):
            if len(levels) == level:
                levels.append([])
            dummy = root
            while root:
                levels[level].append(root.val)
                root = root.next
            if dummy and dummy.left:
                level_order(dummy.left, level + 1)

        level_order(node_root, 0)
        node_list = []
        for level in levels:
            for item in level:
                node_list.append(item)
            if node_list:
                node_list.append(None)
        return node_list
