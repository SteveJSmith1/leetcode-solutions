#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:15:47 2017

@author: SteveJSmith1
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Returns length of last word in a string if it exists
        
        :type s: str
        :rtype: int
        """
        
        try:
            words = s.split()
            return len(words[-1])
        except:
            return 0
    
    



from nose.tools import assert_equal


class TestLengthOfLastWord(object):

    def test_lengthOfLastWord(self):
        solution = Solution()
        
        assert_equal(solution.lengthOfLastWord("Hello World"), 5)
        assert_equal(solution.lengthOfLastWord(""), 0)
        assert_equal(solution.lengthOfLastWord(" "), 0)
        assert_equal(solution.lengthOfLastWord("Hello World "), 5)
        assert_equal(solution.lengthOfLastWord("testing blank at end "), 3)
        
        
        
        
        
        
        print('Success: test_lengthOfLastWord')


def main():
    test = TestLengthOfLastWord()
    test.test_lengthOfLastWord()


if __name__ == '__main__':
    main()
       