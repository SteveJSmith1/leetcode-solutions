#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:11:11 2017

@author: SteveJSmith1

Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in 
the array, and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for num in nums:
            if nums.count(num) > 1:
                return True
        return False
    
from nose.tools import assert_equal


class TestContainsDuplicate(object):

    def test_containsDuplicate(self):
        solution = Solution()
        
        assert_equal(solution.containsDuplicate([1,2,3,4,5]), False)
        assert_equal(solution.containsDuplicate([]), False)
        assert_equal(solution.containsDuplicate([1,2,2,3,4,5]), True)
        assert_equal(solution.containsDuplicate([2,1,3,2,1,5]), True)
        
               
        
        print('Success: test_containsDuplicate')


def main():
    test = TestContainsDuplicate()
    test.test_containsDuplicate()


if __name__ == '__main__':
    main()
       
 