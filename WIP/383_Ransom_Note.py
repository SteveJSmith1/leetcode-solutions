#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:58:19 2017

@author: SteveJSmith1

Given an arbitrary ransom note string and another string containing 
letters from all the magazines, write a function that will return true 
if the ransom note can be constructed from the magazines ; otherwise, 
it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Convert the strings to sorted lists
        sr = sorted(ransomNote)
        sn = sorted(magazine)
        # Check if element in second list
        for val in sr:
            if val in sn:
                sn.remove(val)
            else:
                return False
        return True
 
    
from nose.tools import assert_equal


class TestCanConstruct(object):

    def test_canConstruct(self):
        solution = Solution()
        
        assert_equal(solution.canConstruct("a", "b"), False)
        assert_equal(solution.canConstruct("aa", "ab"), False)
        assert_equal(solution.canConstruct("aa", "aab"), True)
        assert_equal(solution.canConstruct("ransom note","sansomr tone"), True)
        
        print('Success: test_canConstruct')


def main():
    test = TestCanConstruct()
    test.test_canConstruct()


if __name__ == '__main__':
    main()
       
 
