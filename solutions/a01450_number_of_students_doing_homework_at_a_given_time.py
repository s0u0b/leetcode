"""
Problem:
    1450. Number of Students Doing Homework at a Given Time
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time
Tags:
    Array
Date:
    2022-05-10T14:11:00.877308+08:00
"""
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ans = ans + 1
        return ans


tests = [
    (
        ([1, 2, 3], [3, 2, 7], 4,
         ),
        1,
    ),
    (
        ([4], [4], 4,
         ),
        1,
    ),
]
