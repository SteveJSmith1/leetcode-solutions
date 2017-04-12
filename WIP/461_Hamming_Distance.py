#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:43:11 2017

@author: SteveJSmith1

"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        The Hamming distance between two integers is the number of positions 
        at which the corresponding bits are different.

        Given two integers x and y, calculate the Hamming distance.
        
        Input: x = 1, y = 4

        Output: 2
        
        Explanation:
        1   (0 0 0 1)
        4   (0 1 0 0)
               ↑   ↑
        
        :type x: int
        :type y: int
        :rtype: int
        """
        bs = bin(x^y) # XOR and convert to binary string
        # the hamming number is the number of 1s in the XOR string
        count = [c for c in bs if c=='1']
        return len(count)


   
from nose.tools import assert_equal


class TestHammingDistance(object):

    def test_hammingDistance(self):
        solution = Solution()
        
        assert_equal(solution.hammingDistance(1,4), 2)
        assert_equal(solution.hammingDistance(10,40), 2)
        assert_equal(solution.hammingDistance(100,130), 5)
        assert_equal(solution.hammingDistance(998,4567), 5)
        
        print('Success: test_hammingDistance')


def main():
    test = TestHammingDistance()
    test.test_hammingDistance()


if __name__ == '__main__':
    main()
       