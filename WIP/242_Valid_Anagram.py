#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:21:45 2017

@author: SteveJSmith1

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = sorted(list(s))
        lt = sorted(list(t))
        return ls == lt

    
from nose.tools import assert_equal


class TestIsAnagram(object):

    def test_isAnagram(self):
        solution = Solution()
        
        assert_equal(solution.isAnagram("",""), True)
        assert_equal(solution.isAnagram("anagram","nanagram"), False)
        assert_equal(solution.isAnagram("anagram","naagram"), True)
        print('Success: test_isAnagram')


def main():
    test = TestIsAnagram()
    test.test_isAnagram()


if __name__ == '__main__':
    main()
       
 