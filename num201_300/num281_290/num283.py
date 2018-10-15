#encoding:utf8
__author__ = 'gold'

'''
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        index = 0
        while index < len(nums):
            while index < len(nums) and nums[index] != 0:
                index += 1
            mid = index
            while mid < len(nums) and nums[mid] == 0:
                mid += 1

            if mid == len(nums):
                break

            end = mid
            while index < mid and  end < len(nums) and nums[end] != 0:
                nums[index] = nums[end]
                nums[end] = 0
                end += 1
                index += 1


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        left = 0
        right = 0
        while left < len(nums):
            if nums[left] != 0:
                left += 1
                continue
            right = max(right,left)
            while right < len(nums) and nums[right] == 0:
                right += 1
            if right == len(nums):
                return
            nums[left],nums[right] = nums[right],nums[left]
            left += 1


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    nums = [1,2,3,4,5,6,7,8,9,0]
    nums = [0,0,0,0,0]
    Solution().moveZeroes(nums)
    print(nums)
    Solution().moveZeroes([1])