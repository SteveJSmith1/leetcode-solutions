#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:15:07 2017

@author: SteveJSmith1

Given scores of N athletes, find their relative ranks and the people with 
the top three highest scores, who will be awarded medals: 
    "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, 
so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks 
according to their scores.

Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

"""
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Sort the nums in reversed order
        snums = sorted(nums)[::-1]
        # Ascertain ranks
        ranks = [i + 1 for i, val in enumerate(snums)]
        # Create dict with values and the rank
        vals = dict()
        for i, val in enumerate(ranks):
            if val == 1:
                vals[snums[i]] = "Gold Medal"
            elif val == 2:
                vals[snums[i]] = "Silver Medal"
            elif val == 3:
                vals[snums[i]] = "Bronze Medal"
            else:
                vals[snums[i]] = str(val)
        # Look up dict values for vals in nums
        awards = [vals[val] for val in nums]
                
        return awards



from nose.tools import assert_equal


class TestFindRelativeRanks(object):

    def test_findRelativeRanks(self):
        solution = Solution()
        
        assert_equal(solution.findRelativeRanks([5,4,3,2,1]), 
                     ["Gold Medal","Silver Medal","Bronze Medal","4","5"])
        assert_equal(solution.findRelativeRanks([10,9]), 
                     ["Gold Medal","Silver Medal"])
        assert_equal(solution.findRelativeRanks([]), [])
        assert_equal(solution.findRelativeRanks([10,3,8,9,4]), 
                     ["Gold Medal","5","Bronze Medal","Silver Medal","4"])
        print('Success: test_findRelativeRanks')


def main():
    test = TestFindRelativeRanks()
    test.test_findRelativeRanks()


if __name__ == '__main__':
    main()
       
 
