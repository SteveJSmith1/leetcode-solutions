#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:40:46 2017

@author: SteveJSmith1
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        Given a word, you need to judge whether the usage of capitals in 
        it is right or not.

        We define the usage of capitals in a word to be right when one of 
        the following cases holds:

            All letters in this word are capitals, like "USA".
            All letters in this word are not capitals, like "leetcode".
            Only the first letter in this word is capital if it has more than 
            one letter, like "Google".
        
        Otherwise, we define that this word doesn't use capitals in a right way.
        :type word: str
        :rtype: bool
        """
        # Convert characters to list
        lw = list(word)
        # if a char is a uppercase, return 1, else 0
        for idx, char in enumerate(lw):
            if char.isupper():
                lw[idx] = 1
               
            else:
                lw[idx] = 0
                 
        # Process array
         
        if sum(lw) == len(lw):
            return True
        elif lw[0] == 1 and sum(lw) == 1:
            return True
        else:
            return False

        


from nose.tools import assert_equal


class TestDetectCapitalUse(object):

    def test_detectCapitalUse(self):
        solution = Solution()
        
        assert_equal(solution.detectCapitalUse("USA"), True)
        assert_equal(solution.detectCapitalUse("FlaG"), False)
        assert_equal(solution.detectCapitalUse("Chips"), True)
       
        print('Success: test_detectCapitalUse')


def main():
    test = TestDetectCapitalUse()
    test.test_detectCapitalUse()


if __name__ == '__main__':
    main()
       
 