#encoding:utf8
__author__ = 'gold'

'''
368. Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
'''

class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        nums.sort()
        dpList = []
        dpList.append([1,-1])
        for i in range(1,len(nums)):
            maxFactor = 0
            index = -1
            for j in range(i):
                if nums[j] > nums[i]*.5 + 1:
                    break
                if nums[i] % nums[j] == 0:
                    if maxFactor < dpList[j][0]:
                        maxFactor = dpList[j][0]
                        index = j
            dpList.append([maxFactor + 1,index])

        maxFactor = 0
        index = -1
        for i in range(len(nums)):
            if maxFactor < dpList[i][0]:
                maxFactor = dpList[i][0]
                index = i
        res = []
        while True:
            res.append(nums[index])
            index = dpList[index][1]
            if index < 0 :
                break
        return res

class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) <= 1:
            return nums

        ans = []
        nums.sort()
        numPathDict = {}
        for num in nums:
            path = [num]
            flag = num * .5 + 1
            index = 0
            while nums[index] < flag:
                if num % nums[index] == 0:
                    if nums[index] in numPathDict and len(path) < len(numPathDict[nums[index]]) + 1:
                        path = numPathDict[nums[index]] + [num]
                    if num // nums[index] in numPathDict and len(path) < len(numPathDict[num // nums[index]]) + 1:
                        path = numPathDict[num // nums[index]] + [num]
                index += 1
            numPathDict[num] = path
            if len(path) > len(ans):
                ans = path
        return ans

if __name__ == '__main__':
    # print(Solution().largestDivisibleSubset([1,2,3]))
    # print(Solution().largestDivisibleSubset([1,2,4,8]))
    print(Solution().largestDivisibleSubset([2,3,4,5,6,7,8]))
    print(Solution().largestDivisibleSubset([2]))
    print(Solution().largestDivisibleSubset([3,4,16,8]))