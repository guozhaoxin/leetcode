#encoding:utf8
__author__ = 'gold'

'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        if len(nums) < 4:
            return results
        nums.sort()
        if nums[0] + nums[1] + nums[2] + nums[3] > target or nums[-1]+ nums[-2] + nums[-3] + nums[-4] < target:
            return results

        left = 0
        while left < len(nums) - 3:
            right = len(nums) - 1
            while left < right - 2:
                mid1 = left + 1
                mid2 = right - 1
                diff = target - nums[left] - nums[right]
                while mid1 < mid2:
                    if nums[mid2] + nums[mid1] == diff:
                        results.append([nums[left],nums[mid1],nums[mid2],nums[right]])
                        temp = nums[mid1]
                        mid1 += 1
                        while mid1 < mid2 and temp == nums[mid1]:
                            mid1 += 1

                        temp = nums[mid2]
                        mid2 -= 1
                        while mid1 < mid2 and temp == nums[mid2]:
                            mid2 -= 1
                    elif nums[mid1] + nums[mid2] < diff:
                        temp = nums[mid1]
                        mid1 += 1
                        while mid1 < mid2 and temp == nums[mid1]:
                            mid1 += 1
                    else:
                        temp = nums[mid2]
                        mid2 -= 1
                        while mid1 < mid2 and temp == nums[mid2]:
                            mid2 -= 1
                left4Sum = nums[left] * 4
                right4Sum = nums[right] * 4
                if left4Sum > target or right4Sum < target:
                    break
                temp = nums[right]
                right -= 1
                while right > left + 2 and nums[right] == temp:
                    right -= 1
            temp = nums[left]
            left += 1
            while left < len(nums) - 3 and nums[left] == temp:
                left += 1
        return results

if __name__ == '__main__':
    nums = [1,-2,-5,-4,-3,3,3,5]
    print(Solution().fourSum(nums,-11))
