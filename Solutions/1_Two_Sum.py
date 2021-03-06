#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:35:26 2017

@author: SteveJSmith1
"""



class Solution(object):
    def twoSum(self, nums, target):
        """
        Given an array of integers, return indices of the two numbers 
        such that they add up to a specific target.
        You may assume that each input would have exactly one solution, 
        and you may not use the same element twice.
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Raising input errors
        if nums == None or target == None:
            raise TypeError("nums and target cannot be NoneType")
        if not nums:
            raise ValueError("nums cannot be empty")
        
        # Enumerate then brute force checking each element pair
        vals = list(enumerate(nums))

        for idx, n in vals:
            for idx2, n2 in vals:
                if n + n2 == target:
                    # Check if indexes are equal
                    if idx != idx2:
                        return([idx, idx2])
                    else:
                        continue
        return None
                
from nose.tools import assert_equal, assert_raises


class TestTwoSum(object):

    def test_twoSum(self):
        solution = Solution()
        
        assert_equal(solution.twoSum([2, 7, 11, 15], 9), [0,1])
        assert_equal(solution.twoSum([-4, 7, 11, 15], 18), [1,2])
        assert_equal(solution.twoSum([-2, 7, 11, 15], 9), [0,2])
        assert_raises(TypeError, solution.twoSum, None)
        assert_raises(TypeError, solution.twoSum, [])
        assert_raises(TypeError, solution.twoSum, ['2'])
        
        
        print('Success: test_twoSum')


def main():
    test = TestTwoSum()
    test.test_twoSum()


if __name__ == '__main__':
    main()
       
 