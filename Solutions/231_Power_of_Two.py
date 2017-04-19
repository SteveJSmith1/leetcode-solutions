#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:55:31 2017

@author: SteveJSmith1
Given an integer, write a function to determine if it is a power of two.
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        
        if a number is a power of two then in it's binary
        form, there is only one 1
        """
        if n <= 0:
            return False
        
        binstring = str(bin(n)[2:])
        return binstring.count('1') == 1


from nose.tools import assert_equal


class TestIsPowerOfTwo(object):

    def test_isPowerOfTwo(self):
        solution = Solution()
        
        assert_equal(solution.isPowerOfTwo(1), True)
        assert_equal(solution.isPowerOfTwo(0), False)
        assert_equal(solution.isPowerOfTwo(-4), False)
        assert_equal(solution.isPowerOfTwo(4), True)
        assert_equal(solution.isPowerOfTwo(1025), False)
        print('Success: test_isPowerOfTwo')


def main():
    test = TestIsPowerOfTwo()
    test.test_isPowerOfTwo()


if __name__ == '__main__':
    main()
       
 