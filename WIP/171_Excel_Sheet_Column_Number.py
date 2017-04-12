#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 12:26:17 2017

@author: SteveJSmith1
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        return

from nose.tools import assert_equal


class TestTitleToNumber(object):

    def test_titleToNumber(self):
        solution = Solution()
        
        assert_equal(solution.titleToNumber("CNFF"), 62354)
        assert_equal(solution.titleToNumber("NC"), 367)
        assert_equal(solution.titleToNumber("L"), 12)
        assert_equal(solution.titleToNumber("Z"), 26)
        
        print('Success: test_titleToNumber')


def main():
    test = TestTitleToNumber()
    test.test_titleToNumber()


if __name__ == '__main__':
    main()
       
 
 