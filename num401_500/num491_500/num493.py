#encoding:utf8
__author__ = 'gold'

'''
493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
'''


class Solution1:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for j in range(len(nums)):
            for i in range(j):
                if nums[j] * 2 < nums[i]:
                    count += 1

        return count


if __name__ == '__main__':
    print(Solution1().reversePairs([1,3,2,3,1]))
    print(Solution1().reversePairs([2,4,3,5,1]))