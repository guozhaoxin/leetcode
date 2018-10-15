#encoding:utf8
__author__ = 'gold'

'''
Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        if not nums:
            return False

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                if mid < len(nums) and nums[mid] < nums[mid + 1]:
                    left = mid + 1
                else:
                    return False
            else:
                if mid > 0 and nums[mid] > nums[mid - 1]:
                    right = mid - 1
                else:
                    return False

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l]:
                l += 1
            elif nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

def p(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return True

    return False

if __name__ == '__main__':
    import random
    for i in range(100):
        nums = []
        for i in range(20):
            nums.append(random.randrange(0,20))
        nums.sort()
        nums = nums[5:] + nums[0:5]

        results = []
        results.append(p(nums,1))
        results.append(Solution().search(nums,1))
        if results[0] != results[1]:
            print(nums,1,results)

        results = []
        results.append(p(nums, 10))
        results.append(Solution().search(nums, 10))
        if results[0] != results[1]:
            print(nums, 10, results)

        results = []
        results.append(p(nums, 19))
        results.append(Solution().search(nums, 19))
        if results[0] != results[1]:
            print(nums, 19, results)

    # nums = [4, 5, 5, 6, 8, 9, 11, 13, 13, 14, 16, 18, 18, 19, 19, 2, 3, 3, 3, 3]
    # Solution().search(nums,19)
    nums = [6, 7, 8, 8, 8, 10, 11, 13, 14, 15, 17, 17, 18, 18, 18, 0, 1, 2, 2, 5]
    # print(Solution().search(nums,1))