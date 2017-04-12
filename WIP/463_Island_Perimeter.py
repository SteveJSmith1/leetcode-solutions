#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:08:02 2017

@author: SteveJSmith1
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if (grid is None or len(grid) == 0 or len(grid[0]) == 0):
            return 0
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Find a 1 and give it length of four
                    result += 4
                    # subtract values based on neighbours
                    if (i > 0 and grid[i-1][j] == 1):
                        result -= 2
                    if (j > 0 and grid[i][j-1] == 1):
                        result -= 2
        return result


from nose.tools import assert_equal


class TestIslandPerimeter(object):

    def test_islandPerimeter(self):
        solution = Solution()
        
        assert_equal(solution.islandPerimeter([[0,1,0,0],
                                               [1,1,1,0],
                                               [0,1,0,0],
                                               [1,1,0,0]]), 16)
        assert_equal(solution.islandPerimeter([[0,1,0],
                                               [1,1,1],
                                               [0,1,0]]), 12)
        assert_equal(solution.islandPerimeter([[0,1],
                                               [1,1]]), 8)
        
        
        print('Success: test_islandPerimeter')


def main():
    test = TestIslandPerimeter()
    test.test_islandPerimeter()


if __name__ == '__main__':
    main()
       
 
 