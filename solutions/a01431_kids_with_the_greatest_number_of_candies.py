"""
Problem:
    1431. Kids With the Greatest Number of Candies
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
Tags:
    Array
Date:
    2022-05-10T14:10:52.270840+08:00
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        is_greatest_among_the_kids = []
        max_candies = max(candies)
        for candy in candies:
            if int(candy) + int(extraCandies) >= max_candies:
                is_greatest_among_the_kids += [True]
            else:
                is_greatest_among_the_kids += [False]
        return is_greatest_among_the_kids


tests = [
    (
        ([2, 3, 5, 1, 3], 3,
         ),
        [True, True, True, False, True],
    ),
    (
        ([4, 2, 1, 1, 2], 1,
         ),
        [True, False, False, False, False],
    ),
    (
        ([12, 1, 12], 10,
         ),
        [True, False, True],
    ),
]
