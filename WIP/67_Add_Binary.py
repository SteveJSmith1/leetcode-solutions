#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:01:49 2017

@author: SteveJSmith1
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        Given two binary strings, return their sum (also a binary string).


        :type a: str
        :type b: str
        :rtype: str
        """
        


from nose.tools import assert_equal


class TestAddBinary(object):

    def test_addBinary(self):
        solution = Solution()
        
        assert_equal(solution.addBinary("11", "1"), "100")
        assert_equal(solution.addBinary("0", "0"), "0")
        assert_equal(solution.addBinary("10101101", "11110"),"11001011")
         
        print('Success: test_addBinary')


def main():
    test = TestAddBinary()
    test.test_addBinary()


if __name__ == '__main__':
    main()
       
 