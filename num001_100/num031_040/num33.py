#encoding:utf8
__author__ = 'gold'

'''
Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find(nums,left,right,target):
            if target < nums[left] or target > nums[right]:
                return -1

            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left += 1
                else:
                    right -= 1
            if nums[left] == target:
                return left
            return -1

        if not nums:
            return -1

        if len(nums) == 1:
            return find(nums,0,0,target)

        if nums[-1] > nums[0]:
            return find(nums,0,len(nums) - 1,target)

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[0]:
                left = mid + 1
            elif nums[mid] == nums[0]:
                left += 1
            else:
                if nums[mid - 1] >= nums[0]:
                    break
                else:
                    right -= 1

        splitIndex = (left + right) // 2
        if target < nums[splitIndex] or target > nums[splitIndex - 1]:
            return -1

        elif target < nums[0]:
            return find(nums,splitIndex,len(nums) - 1,target)
        else:
            return find(nums,0,splitIndex - 1,target)


if __name__ == '__main__':
    ums = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    ums = [1,2]
    target = 0
    ums = [3,1]
    target = 1
    ums = [4,5,1,2,3]
    target = 1
    ums = [3]
    target = 3
    print(Solution().search(ums,target))
