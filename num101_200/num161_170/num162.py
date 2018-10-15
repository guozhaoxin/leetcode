#encoding:utf8
__author__ = 'gold'

'''
Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
'''


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0

        index = 1
        while index < len(nums):
            if nums[index] > nums[index - 1]:
                index += 1
            else:
                break
        return index - 1

if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().findPeakElement(nums))
    print(Solution().findPeakElement([1,2,1,3,5,6,4]))
    print(Solution().findPeakElement([5,4,3,2,1]))
    print(Solution().findPeakElement([5]))