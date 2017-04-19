#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:25:16 2017

@author: SteveJSmith1
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert string to list
        s = list(s)
        # Extract indices and reversed vowels
        idx = [index for index, char in enumerate(s) if char in "aeiouAEIOU"]
        reversed_vowels = [char for index, char in enumerate(s) if char in "aeiouAEIOU"][::-1]
        # Zip these together and pop the character at the index before inserting
        # the char from reversed_vowels at that index
        for i, v in zip(idx, reversed_vowels):
            s.pop(i)
            s.insert(i, v)
        # Join the characters in the list
        return ''.join(s)
    
from nose.tools import assert_equal


class TestReverseVowels(object):

    def test_reverseVowels(self):
        solution = Solution()
        
        assert_equal(solution.reverseVowels("hello"), "holle")
        assert_equal(solution.reverseVowels("leetcode"), "leotcede")
        assert_equal(solution.reverseVowels(""), "")
        assert_equal(solution.reverseVowels("sky"), "sky")
        assert_equal(solution.reverseVowels("cat"), "cat")
        assert_equal(solution.reverseVowels("leet sky cat"), "laet sky cet")
        assert_equal(solution.reverseVowels("An Invitation"), "on invatitIAn")
        print('Success: test_reverseVowels')


def main():
    test = TestReverseVowels()
    test.test_reverseVowels()

if __name__ == "__main__":
    main()