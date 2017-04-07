#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:35:58 2017

@author: SteveJSmith1
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        Given a list of numbers and a target value, 
        return the index if the target is found. If not, return the 
        index where it would be if it were inserted in order.
        
        
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        """
        # Check for valid inputs
        if nums is None or target is None:
            raise TypeError("nums or target can not be None")
        if type(nums) != list:
            raise TypeError("nums must be supplied in a list [0,1,..]")
        # append the target to a list
        nums.append(target)
        # apply index on the sorted set 
        return sorted(set(nums)).index(target)
    


from nose.tools import assert_equal, assert_raises


class TestSearchInsert(object):

    def test_searchInsert(self):
        solution = Solution()
        assert_raises(TypeError, solution.searchInsert, None)
        assert_raises(TypeError, solution.searchInsert, 3, 5)
        assert_equal(solution.searchInsert([1,3,5,6], 0), 0)
        assert_equal(solution.searchInsert([1,3,5,6], 7), 4)
        assert_equal(solution.searchInsert([1,3,5,6], 2), 1)
        assert_equal(solution.searchInsert([1,3,5,6], 5), 2)
        
        print('Success: test_find_diff')


def main():
    test = TestSearchInsert()
    test.test_searchInsert()


if __name__ == '__main__':
    main()

