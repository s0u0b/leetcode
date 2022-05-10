"""
Problem:
    1464. Maximum Product of Two Elements in an Array
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array
Tags:
    Array, Sorting, Heap (Priority Queue)
Date:
    2022-05-10T14:11:08.056212+08:00
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_len = range(len(nums))
        test_list = [[x, y] for x in nums_len for y in nums_len if x != y]
        ans = 0
        for test_case in test_list:
            value = (nums[test_case[0]] - 1) * (nums[test_case[1]] - 1)
            if ans < value:
                ans = value
        return ans


tests = [
    (
        ([3, 4, 5, 2],
         ),
        12,
    ),
    (
        ([1, 5, 4, 5],
         ),
        16,
    ),
    (
        ([3, 7],
         ),
        12,
    ),
]
