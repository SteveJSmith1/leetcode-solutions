#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:58:02 2017

@author: steve
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        return 
    

from nose.tools import assert_equal, assert_raises


class TestIsPalindrome(object):

    def test_isPalindrome(self):
        solution = Solution()
        
        assert_equal(solution.isPalindrome(12321), True)
        assert_equal(solution.isPalindrome(12343), False)
        assert_equal(solution.isPalindrome(-24542), False)
        assert_raises(TypeError, solution.isPalindrome, None)
        assert_raises(TypeError, solution.isPalindrome, "3")
        
        
        print('Success: test_isPalindrome')


def main():
    test = TestIsPalindrome()
    test.test_isPalindrome()


if __name__ == '__main__':
    main()
       
 