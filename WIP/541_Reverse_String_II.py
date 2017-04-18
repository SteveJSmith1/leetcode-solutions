#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:48:03 2017

@author: SteveJSmith1

Given a string and an integer k, you need to reverse the first k characters 
for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them.
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
           s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)


from nose.tools import assert_equal


class TestReverseStr(object):

    def test_reverseStr(self):
        solution = Solution()
        
        assert_equal(solution.reverseStr("abcdefg", 2), "bacdfeg")
        assert_equal(solution.reverseStr("abcdefg", 10), "gfedcba")
        assert_equal(solution.reverseStr("race a car", 4), "ecar a cra")
        print('Success: test_reverseStr')


def main():    

    test = TestReverseStr()
    test.test_reverseStr()
