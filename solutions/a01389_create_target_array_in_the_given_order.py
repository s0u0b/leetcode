"""
Problem:
    1389. Create Target Array in the Given Order
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/create-target-array-in-the-given-order
Tags:
    Array, Simulation
Date:
    2022-05-10T14:10:47.300306+08:00
"""
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i in range(len(index)):
            ans.insert(index[i], nums[i])
        return ans


tests = [
    (
        ([0, 1, 2, 3, 4], [0, 1, 2, 2, 1],
         ),
        [0, 4, 1, 3, 2],
    ),
    (
        ([1, 2, 3, 4, 0], [0, 1, 2, 3, 0],
         ),
        [0, 1, 2, 3, 4],
    ),
    (
        ([1], [0],
         ),
        [1],
    ),
]
