#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:22:17 2017

@author: SteveJSmith1

Given an integer, write a function to determine if it is a power of three.
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        from math import log
        val = round(log(n)/log(3),1)
        print(val)
        return val % 1 == 0
    

from nose.tools import assert_equal


class TestIsPowerOfThree(object):

    def test_isPowerOfThree(self):
        solution = Solution()
        
        assert_equal(solution.isPowerOfThree(27), True)
        assert_equal(solution.isPowerOfThree(1), True)
        assert_equal(solution.isPowerOfThree(0), False)
        assert_equal(solution.isPowerOfThree(11), False)
        assert_equal(solution.isPowerOfThree(45), False)
        assert_equal(solution.isPowerOfThree(-3), False)
        assert_equal(solution.isPowerOfThree(243), True)
        
        print('Success: test_isPowerOfThree')


def main():
    test = TestIsPowerOfThree()
    test.test_isPowerOfThree()


if __name__ == '__main__':
    main()
       
 