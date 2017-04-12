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
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        valid_words = []
        # Apply to all the words in the list
        for word in words:
            # Fetch the row number for the first character
            for i in range(3):
                if word[0].lower() in rows[i]:
                    row_num = i
                    
            # check if characters in word are from same row
            for char in word:
                if char.lower() in rows[row_num]:
                    continue
                else:
                # Break at first exception
                    word = None
            # Append word if all chars in same row
            valid_words.append(word)
        # Remove None from list    
        return [word for word in valid_words if word is not None]
    


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
       