#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:15:47 2017

@author: SteveJSmith1
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return
        



from nose.tools import assert_equal, assert_raises


class TestLengthOfLastWord(object):

    def test_lengthOfLastWord(self):
        solution = Solution()
        
        assert_equal(solution.lengthOfLastWord("Hello World"), 5)
        assert_equal(solution.lengthOfLastWord(""), 0)
        assert_equal(solution.lengthOfLastWord(" "), 0)
        assert_raises(TypeError, solution.lengthOfLastWord, None)
        
        
        
        print('Success: test_lengthOfLastWord')


def main():
    test = TestLengthOfLastWord()
    test.test_lengthOfLastWord()


if __name__ == '__main__':
    main()
       