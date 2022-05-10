"""
Problem:
    1539. Kth Missing Positive Number
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/kth-missing-positive-number
Tags:
    Array, Binary Search
Date:
    2022-05-10T14:11:43.662317+08:00
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_len = 0
        pre_num = 1
        while arr:
            current_num = arr.pop(0)
            if missing_len + current_num - pre_num >= k:
                break
            missing_len += current_num - pre_num
            pre_num = current_num + 1
        return pre_num + abs(missing_len - k) - 1


tests = [
    (
        ([2, 3, 4, 7, 11], 5,
         ),
        9,
    ),
    (
        ([1, 2, 3, 4], 2,
         ),
        6,
    ),
]
