#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:25:13 2017

@author: SteveJSmith1

Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they 
add up to the target, where index1 must be less than index2. Please note that 
your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may 
not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        return

    
from nose.tools import assert_equal

class TestTwoSum(object):

    def test_twoSum(self):
        solution = Solution()
        
        assert_equal(solution.twoSum([2,3,4],6), [1,3])
        assert_equal(solution.twoSum([1,4,5,6],5), [1,2])

        print('Success: test_twoSum')


def main():
    test = TestTwoSum()
    test.test_twoSum()


if __name__ == '__main__':
    main()
       
 