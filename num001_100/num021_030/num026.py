#encoding:utf8
__author__ = 'gold'

'''
Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
'''


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        index = 0
        lengthen = 1
        flag = nums[0] #标记当前要对比的数值

        while index < len(nums):
            while index < len(nums) and nums[index] == flag:
                index += 1
            if index == len(nums):
                break
            nums[lengthen] = nums[index]
            lengthen += 1
            flag = nums[index]
            index += 1
        return lengthen

def p(a,l):
    print(a[:l])

if __name__ == '__main__':
    import random
    a = [random.randint(0,10) for i in range(10)]
    a.sort()
    print(a)
    l = Solution().removeDuplicates(a)
    p(a,l)
