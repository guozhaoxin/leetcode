#encoding:utf8
__author__ = 'gold'

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 == 0:
            return (nums1[int(len(nums1) / 2)] + nums1[int(len(nums1) / 2) - 1]) / 2
        return nums1[int(len(nums1) / 2)]

if __name__ == '__main__':
    a = [1,45,2]
    b = [2,5,2,65]
    print(Solution().findMedianSortedArrays(a,b))
