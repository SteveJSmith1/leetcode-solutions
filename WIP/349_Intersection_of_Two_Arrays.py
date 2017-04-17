#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:36:11 2017

@author: SteveJSmith1

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_a = set(nums1)
        set_b = set(nums2)
        return list(set(set_a & set_b))
    
from nose.tools import assert_equal


class TestIntersection(object):

    def test_intersection(self):
        solution = Solution()
        
        assert_equal(solution.intersection([],[]), [])
        assert_equal(solution.intersection([1, 2, 2, 1],[2, 2]), [2])
        assert_equal(solution.intersection([1, 2, 3, 4, 3, 2, 1],
                                           [2, 2, 3, 3, 1]), [1,2,3])
        print('Success: test_intersection')


def main():
    test = TestIntersection()
    test.test_intersection()


if __name__ == '__main__':
    main()
       
