#encoding:utf8
__author__ = 'gold'

'''
260.
Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xorresult = nums[0]
        for i in range(1,len(nums)):
            xorresult ^= nums[i]

        bitFlag = 1
        for i in range(32):
            temp = bitFlag & xorresult
            if temp != 0:
                break
            bitFlag <<= 1
        print(bitFlag)
        firstxor = secondxor = 0
        result = []
        for num in nums:
            temp = bitFlag & num
            if temp == 0:
                firstxor ^= num
            else:
                secondxor ^= num#
        result.append(firstxor)
        result.append(secondxor)
        return result

if __name__ == '__main__':
    print(Solution().singleNumber([1,2,1,3,2,5]))