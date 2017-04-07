#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:02:48 2017

@author: SteveJSmith1
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        Given a sorted array, remove the duplicates in place such that each 
        element appear only once and return the new length.
        
        :type nums: List[int]
        :rtype: int
        """
        return

from nose.tools import assert_equal, assert_raises
  
class TestRemoveDuplicates(object):

    def test_removeDuplicates(self):
        solution = Solution()
        
        assert_equal(solution.removeDuplicates([1,1,2]), [1,2])
        assert_equal(solution.removeDuplicates([1,1,2,2,3,4,5,5,6]), \
                     [1,2,3,4,5,6])
        
        assert_raises(TypeError, solution.removeDuplicates, None)
        assert_raises(TypeError, solution.removeDuplicates, "3")
        
        
        print('Success: test_removeDuplicates')


def main():
    test = TestRemoveDuplicates()
    test.test_removeDuplicates()


if __name__ == '__main__':
    main()
       