#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:27:00 2017

@author: SteveJSmith1
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        return 
    
    
from nose.tools import assert_equal, assert_raises


class TestGenerate(object):

    def test_generate(self):
        solution = Solution()
        
        assert_equal(solution.generate(0), [])
        assert_equal(solution.generate(1), [[1]])
        assert_equal(solution.generate(5), [[1],[1,1],[1,2,1],[1,3,3,1],\
                     [1,4,6,4,1] ])
        assert_raises(TypeError, solution.generate, None)
        assert_raises(TypeError, solution.generate, "3")
        
        
        print('Success: test_generate')


def main():
    test = TestGenerate()
    test.test_generate()


if __name__ == '__main__':
    main()
       
 