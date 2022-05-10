"""
Problem:
    804. Unique Morse Code Words
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/unique-morse-code-words
Tags:
    Array, Hash Table, String
Date:
    2022-05-10T14:08:08.000552+08:00
"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        character_list = 'abcdefghijklmnopqrstuvwxyz'
        morse_word_list = []
        for word in words:
            morse_word = ''
            for i, c in enumerate(word):
                morse_word += morse_list[character_list.find(c)]
            morse_word_list.append(morse_word)
        ans = set(morse_word_list)
        return len(ans)


tests = [
    (
        (["gin", "zen", "gig", "msg"],
         ),
        2,
    ),
    (
        (["a"],
         ),
        1,
    ),
]
