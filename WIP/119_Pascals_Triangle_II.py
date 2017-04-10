#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:43:44 2017

@author: SteveJSmith1
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        Given an index k, return the kth row of the Pascal's triangle.
        
        :type rowIndex: int
        :rtype: List[int]
        """
        return
    
from nose.tools import assert_equal

class TestGetRow(object):

    def test_getRow(self):
        solution = Solution()
        
        assert_equal(solution.getRow(0), [1])
        assert_equal(solution.getRow(3), [1,3,3,1])
        assert_equal(solution.getRow(10), [1,10,45,120,210,252,210,120,45,10,1])
        
        print('Success: test_getRow')


def main():
    test = TestGetRow()
    test.test_getRow()


if __name__ == '__main__':
    main()
       
 