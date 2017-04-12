#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:09:09 2017

@author: SteveJSmith1
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        Write a program that outputs the string representation of 
        numbers from 1 to n.

        But for multiples of three it should output “Fizz” instead of the 
        number and for the multiples of five output “Buzz”. 
        For numbers which are multiples of both three and five output 
        “FizzBuzz”.
        
        :type n: int
        :rtype: List[str]
        """
        return
    
from nose.tools import assert_equal


class TestFizzBuzz(object):

    def test_fizzBuzz(self):
        solution = Solution()
        
        assert_equal(solution.fizzBuzz(1), "1")
        assert_equal(solution.fizzBuzz(10),
                     ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"])
        assert_equal(solution.fizzBuzz(15), 
                     ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz",
                     "11","Fizz","13","14","FizzBuzz"])
        
        
        print('Success: test_fizzBuzz')


def main():
    test = TestFizzBuzz()
    test.test_fizzBuzz()


if __name__ == '__main__':
    main()
       
 
 