"""
Problem:
    1436. Destination City
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/destination-city
Tags:
    Hash Table, String
Date:
    2022-05-10T14:10:55.077763+08:00
"""
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_list = []
        for path in paths:
            city_a = path[0]
            if city_a not in city_list:
                city_list.append(city_a)
        for path in paths:
            for city in path:
                if city not in city_list:
                    return city


tests = [
    (
        ([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
         ),
        "Sao Paulo",
    ),
    (
        ([["B", "C"], ["D", "B"], ["C", "A"]],
         ),
        "A",
    ),
    (
        ([["A", "Z"]],
         ),
        "Z",
    ),
]
