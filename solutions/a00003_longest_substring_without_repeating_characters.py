"""
Problem:
    3. Longest Substring Without Repeating Characters
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        previous_char_index = {}
        longest_substring_length = 0
        left = 0
        for right, char in enumerate(s):
            if char in previous_char_index.keys():
                left = max(left, previous_char_index[char] + 1)
            previous_char_index[char] = right
            longest_substring_length = max(longest_substring_length, right - left + 1)
        return longest_substring_length


tests = [
    (
        ("abcabcbb",
         ),
        3,
    ),
    (
        ("bbbbb",
         ),
        1,
    ),
    (
        ("pwwkew",
         ),
        3,
    ),
]
