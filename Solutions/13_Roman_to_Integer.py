#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:28:38 2017

@author: SteveJSmith1
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Conversion Values
        conv = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50,
                'X' : 10, 'V' : 5, 'I' : 1
                }
        # Ordinance
        order = {'M' : 1, 'D' : 2, 'C' : 3, 'L' : 4,
                'X' : 5, 'V' : 6, 'III' : 7, 'II' : 8, 'I' : 9
                }
        
        vals = []
        for i in range(len(s) - 1):
            # Check if a value is in the incorrect order
            if order[s[i]] > order[s[i + 1]]:
                # look up this value and make negative
                vals.append(-conv[s[i]])
            else:
                vals.append(conv[s[i]])
        # convert last value
        vals.append(conv[s[-1]])      
        
        return sum(vals)
        
        
s = "DCXXI"
test = Solution()
test.romanToInt(s)
"""
Out[8]: 621
correct
"""

s = "MCMXC"

test = Solution()
test.romanToInt(s)
"""
Out[7]: 2210
incorrect
"""

s = 'MCMXCIV'
test = Solution()
test.romanToInt(s)

