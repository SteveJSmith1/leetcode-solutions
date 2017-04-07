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
        if s is None:
            raise TypeError("A string of roman numerals must be passed")
        if type(s) != str:
            raise TypeError("A string of roman numerals must be passed")
        # Conversion Values
        conv = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50,
                'X' : 10, 'V' : 5, 'I' : 1
                }
        # Ordinance
        order = {'M' : 1, 'D' : 2, 'C' : 3, 'L' : 4,
                'X' : 5, 'V' : 6, 'III' : 7, 'II' : 8, 'I' : 9
                }
        for char in s:
            if char not in conv:
                raise ValueError("Roman numerals are: MDCLXVI")
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

from nose.tools import assert_equal, assert_raises


class TestRomanToInt(object):

    def test_romanToInt(self):
        solution = Solution()
        assert_raises(TypeError, solution.romanToInt, None)
        assert_raises(TypeError, solution.romanToInt, 3)
        assert_raises(ValueError, solution.romanToInt, "ZVG")
        assert_equal(solution.romanToInt("DCXXI"), 621)
        assert_equal(solution.romanToInt("MCMXC"), 1990)
        assert_equal(solution.romanToInt('MCMXCIV'), 1994)
        
        
        print('Success: test_romanToInt')


def main():
    test = TestRomanToInt()
    test.test_romanToInt()


if __name__ == '__main__':
    main()
        
