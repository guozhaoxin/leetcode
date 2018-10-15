#encoding:utf8
__author__ = 'gold'

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numDic = {} #记录所有出现的数的个数
        results = [] #记录结果
        for num in nums:
            if num not in numDic:
                numDic[num] = 1
            elif numDic[num] == 1:
                numDic[num] = 2
            elif num == 0:
                numDic[0] = 3

        if 0 in numDic and numDic[0] == 3:
            results.append([0,0,0])
            numDic[0] = 1
        elif 0 in numDic and numDic[0] == 2:
            numDic[0] = 1

        for key in numDic:
            if numDic[key] == 2:
                sum_neg = - key - key
                if sum_neg in numDic:

                    results.append([key,key,sum_neg])
            for second in numDic:
                if second <= key:
                    continue

                third = - key - second
                if third in numDic and third > key and third > second:
                    results.append([key,second,third])
        return results

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))