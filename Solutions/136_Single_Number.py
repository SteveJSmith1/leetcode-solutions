#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:48:37 2017

@author: SteveJSmith1
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        Given an array of integers, every element appears twice except for one.
        Find that single one.

        Note:
            Your algorithm should have a linear runtime complexity.
        
        :type nums: List[int]
        :rtype: int
        """
        # Raise input Errors
        if nums == None:
            raise TypeError("nums must be a list of numbers")
        if type(nums) != list:
            raise TypeError("nums must be a list of numbers")
            
        # Using counter to find single vals
        from collections import Counter
        single_vals = [k for k, v in Counter(nums).items() if v == 1 ]

        return single_vals[0]
    
    
from nose.tools import assert_equal, assert_raises


class TestSingleNumber(object):

    def test_singleNumber(self):
        solution = Solution()
        
        assert_equal(solution.singleNumber([1,2,2,3,3]), 1)
        assert_equal(solution.singleNumber([2,2,3,3,4,5,5]), 4)
        assert_raises(TypeError, solution.singleNumber, None)
        assert_raises(TypeError, solution.singleNumber, "3")
        
        
        print('Success: test_singleNumber')


def main():
    test = TestSingleNumber()
    test.test_singleNumber()


if __name__ == '__main__':
    main()
       
        