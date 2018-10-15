#encoding:utf8
__author__ = 'gold'

'''
Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        end = len(nums1) - 1
        for num in nums2:
            nums1[end] = num
            end -= 1

        nums1.sort()

        if m + n == len(nums1):
            return
        step = len(nums1) - m - n #表示前边有几个0

        index = step
        for i in range(index,len(nums1)):
            nums1[i - step] = nums1[i]
        end = len(nums1) - 1
        while end >= len(nums1) - step:
            nums1[end] = 0
            end -= 1

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0,0,0]
    nums2 = [2,5,6]
    Solution().merge(nums1,4,nums2,3)
    print(nums1)