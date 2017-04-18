#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:44:47 2017

@author: SteveJSmith1

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        return
    
from nose.tools import assert_equal


class TestFirstUniqChar(object):

    def test_firstUniqChar(self):
        solution = Solution()
        
        assert_equal(solution.firstUniqChar("leetcode"), 0)
        assert_equal(solution.firstUniqChar("loveleetcode"), 2)
        assert_equal(solution.firstUniqChar("aallrreeppaattss"), -1)
        print('Success: test_firstUniqChar')


def main():
    test = TestFirstUniqChar()
    test.test_firstUniqChar()


if __name__ == '__main__':
    main()
       
 