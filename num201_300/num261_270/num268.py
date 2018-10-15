#encoding:utf8
__author__ = 'gold'

'''
268.
Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = len(nums)
        for index  in range(len(nums)):
            xor ^= nums[index] ^ index
        return xor

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        naturalSum = len(nums) * (len(nums) + 1) // 2
        return naturalSum - sum(nums)

if __name__ == '__main__':
    print(Solution().missingNumber([3,0,1]))