#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:29:05 2017

@author: SteveJSmith1

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        return
    
from nose.tools import assert_equal


class TestConvertToBase7(object):

    def test_convertToBase7(self):
        solution = Solution()
        
        assert_equal(solution.convertToBase7(100), "202")
        assert_equal(solution.convertToBase7(-7), "-10")
        assert_equal(solution.convertToBase7(0), "0")
        
        print('Success: test_convertToBase7')


def main():
    test = TestConvertToBase7()
    test.test_convertToBase7()


if __name__ == '__main__':
    main()
       
 