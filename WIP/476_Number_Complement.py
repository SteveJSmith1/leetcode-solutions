#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:24:22 2017

@author: SteveJSmith1
"""
class Solution(object):
    def findComplement(self, num):
        """
        Given a positive integer, output its complement number. 
        The complement strategy is to flip the bits of its binary 
        representation.
        
        :type num: int
        :rtype: int
        """
        
        return
    
from nose.tools import assert_equal


class TestFindComplement(object):

    def test_findComplement(self):
        solution = Solution()
        
        assert_equal(solution.findComplement(5), 2)
        assert_equal(solution.findComplement(1), 0)
        assert_equal(solution.findComplement(501), 10)
        assert_equal(solution.findComplement(4367), 3824)
        
        print('Success: test_findComplement')


def main():
    test = TestFindComplement()
    test.test_findComplement()


if __name__ == '__main__':
    main()
       