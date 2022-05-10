"""
Problem:
    1266. Minimum Time Visiting All Points
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/minimum-time-visiting-all-points
Tags:
    Array, Math, Geometry
Date:
    2022-05-10T14:09:36.621102+08:00
"""
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        point1 = point2 = points[0]
        ans = 0
        for point in points:
            point1 = point2
            point2 = point
            time_x = abs(point1[0] - point2[0])
            time_y = abs(point1[1] - point2[1])
            min_time = max(time_x, time_y)
            ans += min_time
        return ans


tests = [
    (
        ([[1, 1], [3, 4], [-1, 0]],
         ),
        7,
    ),
    (
        ([[3, 2], [-2, 2]],
         ),
        5,
    ),
]
