import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

    @classmethod
    def string_to_list_node(cls, string):
        numbers = json.loads(string)
        dummy_root = ListNode(0)
        pointer = dummy_root
        for number in numbers:
            pointer.next = ListNode(number)
            pointer = pointer.next

        head = dummy_root.next
        return head

    @classmethod
    def list_node_to_string(cls, node):
        if not node:
            return "[]"

        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        return "[" + result[:-2] + "]"

    @classmethod
    def list_to_list_node(cls, numbers):
        dummy_root = ListNode(0)
        pointer = dummy_root
        for number in numbers:
            pointer.next = ListNode(number)
            pointer = pointer.next

        head = dummy_root.next
        return head

    @classmethod
    def list_to_list_node_string(cls, numbers):
        return cls.list_node_to_string(cls.list_to_list_node(numbers))
