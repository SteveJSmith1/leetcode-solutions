#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 12:11:27 2017

@author: SteveJSmith1
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        Given a string, determine if it is a palindrome, 
        considering only alphanumeric characters and ignoring cases.
        
        :type s: str
        :rtype: bool
        """
        string = [w.lower() for w in s if w.isalnum()]
        rev_string = string[::-1]
        return string == rev_string
    
from nose.tools import assert_equal


class TestIsPalindrome(object):

    def test_isPalindrome(self):
        solution = Solution()
        
        assert_equal(solution.isPalindrome("A man, a plan, a canal: Panama"), True)
        assert_equal(solution.isPalindrome(""), True)
        assert_equal(solution.isPalindrome("race a car"), False)
        assert_equal(solution.isPalindrome("0P"), False)
        
               
        
        print('Success: test_isPalindrome')


def main():
    test = TestIsPalindrome()
    test.test_isPalindrome()


if __name__ == '__main__':
    main()
       
 