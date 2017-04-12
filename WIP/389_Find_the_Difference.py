#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:13:13 2017

@author: SteveJSmith1
"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        Given two strings s and t which consist of only lowercase letters.

        String t is generated by random shuffling string s and then 
        adding one more letter at a random position.

        Find the letter that was added in t.
        :type s: str
        :type t: str
        :rtype: str
        """
        return list(set(t) - set(s))[0]
    
from nose.tools import assert_equal


class TestFindTheDifference(object):

    def test_findTheDifference(self):
        solution = Solution()
        
        assert_equal(solution.findTheDifference("abcd", "abcde"), "e")
        assert_equal(solution.findTheDifference("qwerty", "qwerty i"), "i")
        assert_equal(solution.findTheDifference("te sti", "te sti g"), "g")
        
        print('Success: test_findTheDifference')


def main():
    test = TestFindTheDifference()
    test.test_findTheDifference()


if __name__ == '__main__':
    main()
       
 
        