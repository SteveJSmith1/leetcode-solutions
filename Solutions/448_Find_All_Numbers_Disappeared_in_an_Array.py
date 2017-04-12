#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:02:42 2017

@author: SteveJSmith1
"""

#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
""" 
Created on Wed Apr 12 15:08:09 2017 
 
@author: SteveJSmith1 
""" 
 
class Solution(object): 
    def findDisappearedNumbers(self, nums): 
        """ 
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),  
        some elements appear twice and others appear once. 
 
        Find all the elements of [1, n] inclusive that do not appear  
        in this array. 
 
        Could you do it without extra space and in O(n) runtime? 
        You may assume the returned list does not count as extra space. 
        :type nums: List[int] 
        :rtype: List[int] 
        """ 
        for i in range(len(nums)):
            # create an index 
            index = abs(nums[i]) - 1
            # make values negative if in index
            nums[index] = -abs(nums[index])
        # return positive values in num
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


    
from nose.tools import assert_equal 
 
 
class TestFindDisappearedNumbers(object): 
 
    def test_findDisappearedNumbers(self): 
        solution = Solution() 
                 
        assert_equal(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]), [5, 6]) 
        assert_equal(solution.findDisappearedNumbers([1,4,2,2,5,6]), [3])
        assert_equal(solution.findDisappearedNumbers([]), [])
        assert_equal(solution.findDisappearedNumbers([1,1]), [2]) 
       
         
        print('Success: test_findDisappearedNumbers') 
 
 
def main(): 
    test = TestFindDisappearedNumbers() 
    test.test_findDisappearedNumbers() 
 
 
if __name__ == '__main__': 
    main() 
        

