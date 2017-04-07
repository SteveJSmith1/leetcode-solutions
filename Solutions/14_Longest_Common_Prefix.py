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

strs = ["test", "testy", "testing", "testicles"]
        
test = Solution()
test.longestCommonPrefix(strs)
