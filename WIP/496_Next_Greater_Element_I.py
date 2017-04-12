#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:37:13 2017

@author: SteveJSmith1
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        You are given two arrays (without duplicates) nums1 and nums2 
        where nums1’s elements are subset of nums2. 
        Find all the next greater numbers for nums1's elements in the 
        corresponding places of nums2.

        The Next Greater Number of a number x in nums1 is the first 
        greater number to its right in nums2. 
        If it does not exist, output -1 for this number.
        
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for idx, val in enumerate(findNums):
            # Start at the element after nums.index(val)
            for i in range(nums.index(val) + 1, len(nums)):
                if nums[i] > val:
                    findNums[idx] = nums[i]
                    # Break as soon as val found
                    break
            else:
                findNums[idx] = -1
                # Continue to next iteration
                continue
                
        return findNums
 
from nose.tools import assert_equal


class TestNextGreaterElement(object):

    def test_nextGreaterElement(self):
        solution = Solution()
        
        assert_equal(solution.nextGreaterElement([4,1,2], [1,3,4,2]), 
                     [-1,3,-1])
        assert_equal(solution.nextGreaterElement([2,4], [1,2,3,4]),
                     [3,-1])
        assert_equal(solution.nextGreaterElement([4,1,2,3,5],[1,3,4,2, 5, 6, 7]),
                     [5,3,5,4,6])
        
        
        print('Success: test_nextGreaterElement')


def main():
    test = TestNextGreaterElement()
    test.test_nextGreaterElement()


if __name__ == '__main__':
    main()
       
 
 