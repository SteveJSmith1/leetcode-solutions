#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:07:58 2017

@author: SteveJSmith1

You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ls = list(s)
        if ls.count('A') > 1 or ls.count('L') > 2:
            return False
        return True
    
    
from nose.tools import assert_equal


class TestCheckRecord(object):

    def test_checkRecord(self):
        solution = Solution()
        
        assert_equal(solution.checkRecord("PPALLP"), True)
        assert_equal(solution.checkRecord(""), True)
        assert_equal(solution.checkRecord("PPALLL"), False)
        assert_equal(solution.checkRecord("P"), True)
        
               
        
        print('Success: test_checkRecord')


def main():
    test = TestCheckRecord()
    test.test_checkRecord()


if __name__ == '__main__':
    main()
       
 