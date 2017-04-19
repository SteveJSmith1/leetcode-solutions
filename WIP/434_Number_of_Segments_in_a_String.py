#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:30:27 2017

@author: SteveJSmith1

Worked Solution Available
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()) 
    
from nose.tools import assert_equal


class TestCountSegments(object):

    def test_countSegments(self):
        solution = Solution()
        
        assert_equal(solution.countSegments("Hello, my name is John"), 5)
        assert_equal(solution.countSegments(""), 0)
        assert_equal(solution.countSegments("Foo, bar  "), 2)
        assert_equal(solution.countSegments("Foo, bar!"), 2)
        assert_equal(solution.countSegments("         "), 0)
        
        print('Success: test_countSegments')


def main():
    test = TestCountSegments()
    test.test_countSegments()

if __name__ == '__main__':
    main()
 