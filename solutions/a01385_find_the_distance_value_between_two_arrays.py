"""
Problem:
    1385. Find the Distance Value Between Two Arrays
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/find-the-distance-value-between-two-arrays
Tags:
    Array, Two Pointers, Binary Search, Sorting
Date:
    2022-05-10T14:10:37.332226+08:00
"""
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def searchInsert(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if target < nums[mid]:
                    right = mid - 1
                if nums[mid] < target:
                    left = mid + 1
            else:
                return left

        distance_value = 0
        arr2 = sorted(arr2)
        for num1 in arr1:
            index_in_arr2 = searchInsert(arr2, num1)
            if 0 < index_in_arr2 < len(arr2) - 1:
                if abs(num1 - arr2[index_in_arr2 - 1]) > d and abs(num1 - arr2[index_in_arr2]) > d and abs(
                        num1 - arr2[index_in_arr2 + 1]) > d:
                    distance_value += 1
            if 0 == index_in_arr2:
                if abs(num1 - arr2[index_in_arr2]) > d and abs(num1 - arr2[index_in_arr2 + 1]) > d:
                    distance_value += 1
            if index_in_arr2 == len(arr2) - 1:
                if abs(num1 - arr2[index_in_arr2 - 1]) > d and abs(num1 - arr2[index_in_arr2]) > d:
                    distance_value += 1
            if index_in_arr2 > len(arr2) - 1:
                if abs(num1 - arr2[-1]) > d:
                    distance_value += 1
        return distance_value


tests = [
    (
        ([4, 5, 8], [10, 9, 1, 8], 2,
         ),
        2,
    ),
    (
        ([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3,
         ),
        2,
    ),
    (
        ([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6,
         ),
        1,
    ),
]
