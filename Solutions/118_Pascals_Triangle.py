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
        pt = [ [1], [1,1] ]
        #Return special case for numRows = 1,2
        if numRows == 0:
            return []
        elif numRows == 1:
            return [pt[0]]
        elif numRows == 2:
            return pt
        
        # For the third to the last row
        for r in range(3, numRows + 1):
            # create a list of 1s the length of the row number
            row = [1]*r
            # Change coefficients for values in the list except for
            # the first and last, using values fetched from the previous list
            for i in range(0, r - 2):
                row[i + 1] = pt[r - 2][i] + pt[r - 2][i + 1]
            pt.append(row)
        return pt


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
       
 