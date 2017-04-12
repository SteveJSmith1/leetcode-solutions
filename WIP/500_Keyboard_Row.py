#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:46:21 2017

@author: SteveJSmith1
"""


class Solution(object):
    def findWords(self, words):
        """
        Given a List of words, return the words that can be typed using 
        letters of the alphabet on only one row of a QWERTY keyboard
        
        :type words: List[str]
        :rtype: List[str]
        """
        return
    
from nose.tools import assert_equal


class TestFindWords(object):

    def test_findWords(self):
        solution = Solution()
        
        assert_equal(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]),
                     ["Alaska", "Dad"])
        assert_equal(solution.findWords(["Cheese", "Eating", "TypeWriter"]), 
                     ["TypeWriter"])
        
        print('Success: test_findWords')


def main():
    test = TestFindWords()
    test.test_findWords()


if __name__ == '__main__':
    main()
       