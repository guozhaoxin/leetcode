#encoding:utf8
__author__ = 'gold'

'''
Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
'''


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if not nums:
            return 0

        lengthen = 0
        index = 0
        while index < len(nums):
            while index < len(nums) and nums[index] == val:
                index += 1
            if index == len(nums):
                break
            nums[lengthen] = nums[index]
            lengthen += 1
            index += 1
        return lengthen

def p(a,l):
    print(a[:l])

if __name__ == '__main__':
    import random
    a = [random.randint(0,10) for i in range(10)]
    a.sort()
    print(a)
    l = Solution().removeElement([],3)
    p(a,l)
