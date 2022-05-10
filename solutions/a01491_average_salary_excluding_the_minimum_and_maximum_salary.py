"""
Problem:
    1491. Average Salary Excluding the Minimum and Maximum Salary
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary
Tags:
    Array, Sorting
Date:
    2022-05-10T14:11:26.241559+08:00
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


tests = [
    (
        ([4000, 3000, 1000, 2000],
         ),
        2500.00000,
    ),
    (
        ([1000, 2000, 3000],
         ),
        2000.00000,
    ),
]
