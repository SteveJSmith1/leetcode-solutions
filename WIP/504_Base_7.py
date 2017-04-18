#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:29:05 2017

@author: SteveJSmith1

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        # Using divmod in a recursive loop to fetch the modulus
        dm = divmod(num, 7)
        # Collecting the modulus in a list as strings
        smod = []
        # Modulus is the last value
        smod.append(str(dm[-1]))
        # If the first value is less than seven, it has completed
        while dm[0] >= 7:
            dm = divmod(dm[0], 7)
            # Put strings at front of list
            smod.insert(0, str(dm[-1]))
        # Catch the last value
        smod.insert(0, str(dm[0]))
        # return joined string
        if smod[0] == '0':
            smod.remove('0')
        return ''.join(smod)
    

    
from nose.tools import assert_equal


class TestConvertToBase7(object):

    def test_convertToBase7(self):
        solution = Solution()
        
        assert_equal(solution.convertToBase7(100), "202")
        assert_equal(solution.convertToBase7(-7), "-10")
        assert_equal(solution.convertToBase7(0), "0")
        assert_equal(solution.convertToBase7(6), "6")
        
        print('Success: test_convertToBase7')


def main():
    test = TestConvertToBase7()
    test.test_convertToBase7()


if __name__ == '__main__':
    main()
       
 