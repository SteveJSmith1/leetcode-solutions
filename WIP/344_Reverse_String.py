#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:28:04 2017

@author: SteveJSmith1
"""


class Solution(object):
    def reverseString(self, s):
        """
        Write a function that takes a string as input 
        and returns the string reversed.
        :type s: str
        :rtype: str
        """
        return
    
from nose.tools import assert_equal


class TestReverseString(object):

    def test_reverseString(self):
        solution = Solution()
        
        assert_equal(solution.reverseString("hello"), "olleh")
        assert_equal(solution.reverseString("1"), "1")
        assert_equal(solution.reverseString("TestCase"), "esaCtseT")
        assert_equal(solution.reverseString("Whom'p_er i"), "i re_p'mohW")
        
        print('Success: test_reverseString')


def main():
    test = TestReverseString()
    test.test_reverseString()


if __name__ == '__main__':
    main()
       
 
 
        