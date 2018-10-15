#encoding:utf8
__author__ = 'gold'

'''
Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse = True)
        return nums[k - 1]

'''快排实现'''
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        while True:
            index = self.par(nums,left,right)
            if index == k - 1:
                return nums[index]
            if index > k - 1:
                right = index - 1
            else:
                left = index + 1

    def par(self,nums,left,right):
        l = left + 1
        r = right
        flag = nums[left]

        while l <= r:
            if nums[l] < flag and nums[r] > flag:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
            if nums[l] >= flag:
                l += 1
            if nums[r] <= flag:
                r -= 1

        nums[r],nums[left] = nums[left],nums[r]
        return r

if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4],2))