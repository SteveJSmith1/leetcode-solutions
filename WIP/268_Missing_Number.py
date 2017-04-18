#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:21:44 2017

@author: SteveJSmith1

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant extra space complexity?
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return
    

from nose.tools import assert_equal


class TestMissingNumber(object):

    def test_missingNumber(self):
        solution = Solution()
        
        assert_equal(solution.missingNumber([0, 1, 3]), 2)
        assert_equal(solution.missingNumber([0]), 1)
        assert_equal(solution.missingNumber([0,1,2,3]), 4)
        print('Success: test_missingNumber')


def main():
    test = TestMissingNumber()
    test.test_missingNumber()


if __name__ == '__main__':
    main()
       
 