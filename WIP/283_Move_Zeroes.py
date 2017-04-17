#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:58:42 2017

@author: SteveJSmith1
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        Given an array nums, write a function to move all 0's to the end of it 
        while maintaining the relative order of the non-zero elements.

        For example, given nums = [0, 1, 0, 3, 12], after calling your 
        function, nums should be [1, 3, 12, 0, 0].
        
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i, val in enumerate(nums):
            if val == 0:
                nums.remove(val)
                nums.append(val)
        return nums
    
from nose.tools import assert_equal


class TestMoveZeroes(object):

    def test_moveZeroes(self):
        solution = Solution()
        
        assert_equal(solution.moveZeroes([0,1,0,3,12]), [1,3,12,0,0])
        assert_equal(solution.moveZeroes([]), [])
        assert_equal(solution.moveZeroes([0]), [0])
        assert_equal(solution.moveZeroes([1,4,3,2,5]), [1,4,3,2,5])
        assert_equal(solution.moveZeroes([1,0,2,3,2,0,6]), [1,2,3,2,6,0,0])
        
        print('Success: test_moveZeroes')


def main():
    test = TestMoveZeroes()
    test.test_moveZeroes()


if __name__ == '__main__':
    main()
       
 