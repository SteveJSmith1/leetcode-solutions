#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:41:39 2017

@author: SteveJSmith1
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Given a binary array, find the maximum number 
        of consecutive 1s in this array.
        
        :type nums: List[int]
        :rtype: int
        """
        counter = []
        c = 0
        # increase c by 1 if n = 1 and append to counter
        for n in nums:
            if n == 1:
                c += n
                counter.append(c)
            # reset c if n = 0
            else:
                c = 0
        # sort values
        try:
            s = sorted(counter)
            # return highest
            return s[-1]
        except:
            return 0


from nose.tools import assert_equal


class TestFindMaxConsecutiveOnes(object):

    def test_findMaxConsecutiveOnes(self):
        solution = Solution()
        
        assert_equal(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]), 3)
        assert_equal(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]), 2)
        assert_equal(solution.findMaxConsecutiveOnes([1]), 1)
        assert_equal(solution.findMaxConsecutiveOnes([0]), 0)
        
        print('Success: test_findMaxConsecutiveOnes')


def main():
    test = TestFindMaxConsecutiveOnes()
    test.test_findMaxConsecutiveOnes()


if __name__ == '__main__':
    main()
       
 
 