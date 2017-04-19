#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:15:15 2017

@author: SteveJSmith1
"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        This function checks whether an inputted number is a power of four.
        :type num: int
        :rtype: bool
        
        Algorithm:  Filter out negatives
                    Check binary string for one, '1's and an even number of '0's
        """
        
        if num <= 0:
            return False
                
        return (bin(num)[2:].count('1') == 1 and bin(num)[2:].count('0') % 2 == 0)



# To check if the values we return are correct import this.
from nose.tools import assert_equal

# class name taken from the function in the class above
class TestIsPowerOfFour(object):
    # function name also from the above class
    def test_isPowerOfFour(self):
        # define a varable to call the class where our solution is:
        solution = Solution()
        # use assert_equal(input, expected output)
        # Input: 
            # Call the function() within the class using '.', and the input
        # Output:
            # Expected output
        assert_equal(solution.isPowerOfFour(4), True)
        assert_equal(solution.isPowerOfFour(1), True)
        assert_equal(solution.isPowerOfFour(16), True)
        assert_equal(solution.isPowerOfFour(65536), True)
        assert_equal(solution.isPowerOfFour(0), False)
        assert_equal(solution.isPowerOfFour(-4), False)
        assert_equal(solution.isPowerOfFour(65535), False)
        assert_equal(solution.isPowerOfFour(123456), False)
        # An output to show tests have passed
        print('Success: test_isPowerOfFour')

# Call the tests
def main():
    test = TestIsPowerOfFour()
    test.test_isPowerOfFour()

# Run the tests when file is run
if __name__ == '__main__':
    main()
       
        
