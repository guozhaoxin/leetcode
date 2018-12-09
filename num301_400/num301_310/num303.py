#encoding:utf8
__author__ = 'gold'

'''
303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sumList = [0] * len(nums)
        if not nums:
            self.sumList = None
        else:
            self.sumList[0] = nums[0]
            for index in range(1,len(nums)):
                self.sumList[index] = self.sumList[index - 1] + self.nums[index]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.sumList:
            return
        if i >= len(self.nums):
            return
        if i == 0:
            return self.sumList[j]
        return self.sumList[j] - self.sumList[i - 1]

if __name__ == '__main__':
    obj = NumArray([-2,0,3,-5,2,-1])
    print(obj.sumList)
    print(obj.sumRange(0,2))
    print(obj.sumRange(2,5))
    print(obj.sumRange(0,5))
