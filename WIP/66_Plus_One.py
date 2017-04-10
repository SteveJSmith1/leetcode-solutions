#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:38:45 2017

@author: SteveJSmith1
"""

class Solution(object):
    def plusOne(self, digits):
        """
        Given a non-negative integer represented as a non-empty array of 
        digits, plus one to the integer.

        You may assume the integer do not contain any leading zero, 
        except the number 0 itself.

        The digits are stored such that the most significant digit is at the 
        head of the list.
        
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] = digits[-1] + 1
        return digits
    
from nose.tools import assert_equal, assert_raises


class TestPlusOne(object):

    def test_plusOne(self):
        solution = Solution()
        
        assert_equal(solution.plusOne([1,2,3,4,5,6]), [1,2,3,4,5,7])
        assert_equal(solution.plusOne([0]), [1])
        assert_equal(solution.plusOne([1,1,2]), [1,1,3])
        assert_equal(solution.plusOne([1,0,2,3,4]), [1,0,2,3,5])
        assert_raises(TypeError, solution.plusOne, None)
        assert_raises(TypeError, solution.plusOne, "3")
        
        
        print('Success: test_plusOne')


def main():
    test = TestPlusOne()
    test.test_plusOne()


if __name__ == '__main__':
    main()
       
 