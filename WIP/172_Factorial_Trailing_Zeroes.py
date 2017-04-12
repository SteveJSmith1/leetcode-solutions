#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:24:42 2017

@author: SteveJSmith1
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import factorial
        s = str(factorial(n))
        
        return len(s) - len(s.rstrip('0'))


from nose.tools import assert_equal
    
class TestTrailingZeroes(object):

    def test_trailingZeroes(self):
        solution = Solution()
        
        assert_equal(solution.trailingZeroes(4), 0)
        assert_equal(solution.trailingZeroes(40), 9)
        assert_equal(solution.trailingZeroes(100), 24)
        assert_equal(solution.trailingZeroes(1000), 249)
        
        print('Success: test_trailingZeroes')


def main():
    test = TestTrailingZeroes()
    test.test_trailingZeroes()


if __name__ == '__main__':
    main()
       
 