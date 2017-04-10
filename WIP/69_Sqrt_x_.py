#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:12:15 2017

@author: SteveJSmith1
"""

class Solution(object):
    def mySqrt(self, x):
        """
        Implement int sqrt(int x).

        Compute and return the square root of x.
        :type x: int
        :rtype: int
        """
        return
    
from nose.tools import assert_equal


class TestMySqrt(object):

    def test_mySqrt(self):
        solution = Solution()
        
        assert_equal(solution.mySqrt(0), 0)
        assert_equal(solution.mySqrt(64), 8)
        assert_equal(solution.mySqrt(79), 8)
        print('Success: test_mySqrt')


def main():
    test = TestMySqrt()
    test.test_mySqrt()


if __name__ == '__main__':
    main()