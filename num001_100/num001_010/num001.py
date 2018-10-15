#encoding:utf8
__author__ = 'gold'

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numDict.keys():
                return [numDict[diff],i]
            else:
                numDict[nums[i]] = i


if __name__ == '__main__':
    nums = [1,5,7,9,10,1]
    target = 19
    print(Solution().twoSum(nums,target))