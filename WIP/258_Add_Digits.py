#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:31:02 2017

@author: SteveJSmith1

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        listnum = list(str(num))
        n = 10
        # addDigits total will be 9 or less
        while n > 9:
            # convert to integers and sum
            n = sum([int(v) for v in listnum])
            # change integer to list of digits
            listnum = list(str(n))
        return n

  
from nose.tools import assert_equal


class TestAddDigits(object):

    def test_addDigits(self):
        solution = Solution()
        
        assert_equal(solution.addDigits(38), 2)
        assert_equal(solution.addDigits(0), 0)
        assert_equal(solution.addDigits(345678), 6)
        assert_equal(solution.addDigits(1234567890), 9)
        
               
        
        print('Success: test_addDigits')


def main():
    test = TestAddDigits()
    test.test_addDigits()


if __name__ == '__main__':
    main()
       
