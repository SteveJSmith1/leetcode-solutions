#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 12:26:17 2017

@author: SteveJSmith1
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        Given a column title as appears in an Excel sheet, 
        return its corresponding column number.
        
        :type s: str
        :rtype: int
        """
        # A base 26 alphabet can be constructed by changing the string
        # to base 36 (includes 0-9) subtracting then adding 1
        v = [int(i, 36) - 10 + 1 for i in s]
        
        # reversing the list so the index corresponds to the needed
        # power of 26
        vals = v[::-1]
        
        # apply a power of 26 
        for i in range(0, len(vals)):
            vals[i] = vals[i]*26**i
        # return the sum of the list
        return sum(vals)



from nose.tools import assert_equal


class TestTitleToNumber(object):

    def test_titleToNumber(self):
        solution = Solution()
        
        assert_equal(solution.titleToNumber("CNFF"), 62354)
        assert_equal(solution.titleToNumber("NC"), 367)
        assert_equal(solution.titleToNumber("L"), 12)
        assert_equal(solution.titleToNumber("Z"), 26)
        
        print('Success: test_titleToNumber')


def main():
    test = TestTitleToNumber()
    test.test_titleToNumber()


if __name__ == '__main__':
    main()
       
 
 