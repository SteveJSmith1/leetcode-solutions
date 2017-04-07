#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:08:52 2017

@author: SteveJSmith1
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        return 
    
from nose.tools import assert_equal, assert_raises

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
class TestReverse(object):

    def test_reverse(self):
        solution = Solution()
        
        assert_equal(solution.reverse(123), 321)
        assert_equal(solution.reverse(12343), 34321)
        assert_equal(solution.reverse(-24567), -76542)
        # integers over 32 bit
        assert_equal(solution.reverse(-4147483647), 0)
        assert_equal(solution.reverse(4147483647), 0)
        assert_raises(TypeError, solution.reverse, None)
        assert_raises(TypeError, solution.reverse, "3")
        
        
        print('Success: test_reverse')


def main():
    test = TestReverse()
    test.test_reverse()


if __name__ == '__main__':
    main()
       
 
         
        