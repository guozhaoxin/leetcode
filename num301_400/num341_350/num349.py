#encoding:utf8
__author__ = 'gold'

'''
Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums1.sort()
        nums2.sort()
        result = []
        left1 = 0
        left2 = 0
        while left1 < len(nums1) and left2 < len(nums2):
            if nums1[left1] == nums2[left2]:
                result.append(nums1[left1])
                left1 += 1
                left2 += 1
            elif nums1[left1] < nums2[left2]:
                left1 += 1
            else:
                left2 += 1
        return result

if __name__ == '__main__':
    print(Solution().intersection([1,2,2,1],[2,2]))