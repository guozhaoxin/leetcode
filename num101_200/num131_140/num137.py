#encoding:utf8
__author__ = 'gold'

'''
Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return (sum(set(nums)) * 3 - sum(nums)) // 2

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0
        for i in range(0,64):
            sum = 0
            for num in nums:
                sum += (num >> i) & 1
            result = result | ((sum % 3) << i)
        return result

if __name__ == '__main__':
    nums = [0,1,0,1,0,1,-99]
    # nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    print(Solution().singleNumber(nums))