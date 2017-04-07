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
        
        Do not allocate extra space for another array, 
        you must do this in place with constant memory.
        
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        tail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]

        return tail + 1
    

from nose.tools import assert_equal
  
class TestRemoveDuplicates(object):

    def test_removeDuplicates(self):
        solution = Solution()
        
        assert_equal(solution.removeDuplicates([1,1,2]), 2)
        assert_equal(solution.removeDuplicates([1,1,2,2,3,4,5,5,6]), 6)
        print('Success: test_removeDuplicates')


def main():
    test = TestRemoveDuplicates()
    test.test_removeDuplicates()


if __name__ == '__main__':
    main()
       