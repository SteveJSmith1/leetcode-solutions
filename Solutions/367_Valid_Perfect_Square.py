#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:11:23 2017

@author: SteveJSmith1

Worked Solution Available
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        res = num**0.5
        return res / int(res) == 1
    
from nose.tools import assert_equal


class TestIsPerfectSquare(object):

    def test_isPerfectSquare(self):
        solution = Solution()
        
        assert_equal(solution.isPerfectSquare(0), False)
        assert_equal(solution.isPerfectSquare(1), True)
        assert_equal(solution.isPerfectSquare(-4), False)
        assert_equal(solution.isPerfectSquare(1522756), True)
        assert_equal(solution.isPerfectSquare(1522757), False)
        print('Success: test_isPerfectSquare')


def main():
    test = TestIsPerfectSquare()
    test.test_isPerfectSquare()

if __name__ == '__main__':
    main()
 