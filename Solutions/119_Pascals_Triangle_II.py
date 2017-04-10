#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:43:44 2017

@author: SteveJSmith1
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        Given an index k, return the kth row of the Pascal's triangle.
        
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows = rowIndex + 1
        pt = [ [1], [1,1] ]
        #Return special case for numRows = 1,2
        if numRows == 0:
            return []
        elif numRows == 1:
            return pt[0]
        elif numRows == 2:
            return pt[1]
        
        # For the third to the last row
        for r in range(3, numRows + 1):
            # create a list of 1s the length of the row number
            row = [1]*r
            # Change coefficients for values in the list except for
            # the first and last, using values fetched from the previous list
            for i in range(0, r - 2):
                row[i + 1] = pt[r - 2][i] + pt[r - 2][i + 1]
            pt.append(row)
        return pt[-1]
        
    
from nose.tools import assert_equal

class TestGetRow(object):

    def test_getRow(self):
        solution = Solution()
        
        assert_equal(solution.getRow(0), [1])
        assert_equal(solution.getRow(3), [1,3,3,1])
        assert_equal(solution.getRow(10), [1,10,45,120,210,252,210,120,45,10,1])
        
        print('Success: test_getRow')


def main():
    test = TestGetRow()
    test.test_getRow()


if __name__ == '__main__':
    main()
       
 