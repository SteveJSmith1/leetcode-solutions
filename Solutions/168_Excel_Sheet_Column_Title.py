#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 12:26:17 2017

@author: SteveJSmith1
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        Given a positive integer, return its corresponding column title 
        as appears in an Excel sheet.
        
        :type n: int
        :rtype: str
        """
        title = ''
        alist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while n:
            mod = (n - 1) % 26
            n = int((n - mod) / 26)  
            title += alist[mod]
        return title[::-1]

from nose.tools import assert_equal


class TestConvertToTitle(object):

    def test_convertToTitle(self):
        solution = Solution()
        
        assert_equal(solution.convertToTitle(62354), "CNFF")
        assert_equal(solution.convertToTitle(367), "NC")
        assert_equal(solution.convertToTitle(12), "L")
        assert_equal(solution.convertToTitle(26), "Z")
        
        print('Success: test_convertToTitle')


def main():
    test = TestConvertToTitle()
    test.test_convertToTitle()


if __name__ == '__main__':
    main()
       
 
 