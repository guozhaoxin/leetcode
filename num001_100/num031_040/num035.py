#encoding:utf8
__author__ = 'gold'

'''
Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return 0

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] < target:
            return left + 1
        else:
            return left

if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6],5))
    print(Solution().searchInsert([1,3,5,6],2))
    print(Solution().searchInsert([1,3,5,6],7))
    print(Solution().searchInsert([1,3,5,6],0))
