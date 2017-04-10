#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:19:07 2017

@author: SteveJSmith1
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        
        You are climbing a stair case. It takes n steps to reach to the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        
        Note: Given n will be a positive integer.
        """
        return
    


from nose.tools import assert_equal


class TestClimbStairs(object):

    def test_climbStairs(self):
        solution = Solution()
        
        assert_equal(solution.climbStairs(4), 5)
        assert_equal(solution.climbStairs(0), 1)
        assert_equal(solution.climbStairs(3), 3)
        assert_equal(solution.climbStairs(30), 1346269)

        print('Success: test_climbStairs')


def main():
    test = TestClimbStairs()
    test.test_climbStairs()


if __name__ == '__main__':
    main()
       
 
        