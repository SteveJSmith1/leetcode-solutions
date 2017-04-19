#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:02:45 2017

@author: SteveJSmith1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ln = list(str(n))
        sum_list = []
        sum_n = 0

        while sum_n != 1:
            sum_n = sum([int(i)**2 for i in ln])
            if sum_n in sum_list:
                return False
            sum_list.append(sum_n)
            ln = list(str(sum_n))
  
        return True

from nose.tools import assert_equal


class TestIsHappy(object):

    def test_isHappy(self):
        solution = Solution()
        
        assert_equal(solution.isHappy(19), True)
        assert_equal(solution.isHappy(1), True)
        assert_equal(solution.isHappy(20), False)
        assert_equal(solution.isHappy(123456789), False)
        print('Success: test_isHappy')


def main():
    test = TestIsHappy()
    test.test_isHappy()
    
if __name__ == "__main__":
    main()