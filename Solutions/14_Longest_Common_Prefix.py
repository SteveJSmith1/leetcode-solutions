#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:59:33 2017

@author: SteveJSmith1
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Checks for the longest common prefix in a list of strings
        
        
        :type strs: List[str]
        :rtype: str
        """
        import os
        return os.path.commonprefix(strs)



from nose.tools import assert_equal, assert_raises


class TestLongestCommonPrefix(object):

    def test_longestCommonPrefix(self):
        solution = Solution()
        assert_raises(TypeError, solution.longestCommonPrefix, None)
        assert_raises(TypeError, solution.longestCommonPrefix, 3)
        assert_equal(solution.longestCommonPrefix(\
                                                  ["test", "testy", "testing",\
                                                   "testicles"]),  'test')
        
        print('Success: test_searchInsert')


def main():
    test = TestLongestCommonPrefix()
    test.test_longestCommonPrefix()


if __name__ == '__main__':
    main()

