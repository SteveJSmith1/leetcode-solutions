#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:11:55 2017

@author: SteveJSmith1
"""
class Solution(object):
    def reverseWords(self, s):
        """
        Given a string, you need to reverse the order of characters in each 
        word within a sentence while still preserving whitespace and initial 
        word order.
        
        :type s: str
        :rtype: str
        """
        # Split on whitespace
        spl = s.split()
        # reverse each word
        rev = [s[::-1] for s in spl]
        # join reversed words with whitespace
        return ' '.join(rev)
    
from nose.tools import assert_equal


class TestReverseWords(object):

    def test_reverseWords(self):
        solution = Solution()
        
        assert_equal(solution.reverseWords("Let's take LeetCode contest"),
                     "s'teL ekat edoCteeL tsetnoc")
        assert_equal(solution.reverseWords("ChiPs' and, ChEeSe"),
                     "'sPihC ,dna eSeEhC")
        assert_equal(solution.reverseWords("TuR'Nip"), "piN'RuT")

        print('Success: test_reverseWords')


def main():
    test = TestReverseWords()
    test.test_reverseWords()


if __name__ == '__main__':
    main()
       