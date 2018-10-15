#encoding:utf8
__author__ = 'gold'

'''
Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 3:
            return min(nums)

        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                if nums[mid] < nums[mid - 1]:
                    break
                else:
                    right = mid - 1

        return nums[mid]

if __name__ == '__main__':
    nums =  [3,4,5,1,2]
    print(Solution().findMin(nums))
    print(Solution().findMin([4,5,6,7,0,1,2]))