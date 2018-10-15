#encoding:utf8
__author__ = 'gold'

'''
Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        numDic = {}
        for index in range(len(nums)):
            if nums[index] in numDic:
                numDic[nums[index]].append(index)
                for i in range(len(numDic[nums[index]]) - 1):
                    for j in range(i + 1,len(numDic[nums[index]])):
                        if abs(numDic[nums[index]][j] - numDic[nums[index]][i]) <= k:
                            return True
            else:
                numDic[nums[index]] = [index,]

        return False