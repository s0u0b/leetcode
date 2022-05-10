"""
Problem:
    744. Find Smallest Letter Greater Than Target
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/find-smallest-letter-greater-than-target
Tags:
    Array, Binary Search
Date:
    2022-05-10T14:07:56.800842+08:00
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters) - 1

        def wrap_around(index):
            if index < 0:
                index = -1
            if index > length:
                index = 0
            return index

        length = len(letters) - 1
        left, right = 0, length
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] == target:
                if mid + 1 <= length and letters[mid] == letters[mid + 1]:
                    left = mid + 1
                    continue
                return letters[wrap_around(mid + 1)]
            if target < letters[mid]:
                right = mid - 1
            if letters[mid] < target:
                left = mid + 1
        else:
            return letters[wrap_around(left)]


tests = [
    (
        (["c", "f", "j"], "a",
         ),
        "c",
    ),
    (
        (["c", "f", "j"], "c",
         ),
        "f",
    ),
    (
        (["c", "f", "j"], "d",
         ),
        "f",
    ),
]
