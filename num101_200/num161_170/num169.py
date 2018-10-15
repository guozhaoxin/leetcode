#encoding:utf8
__author__ = 'gold'

'''
Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        haha = {}
        for i in nums:
            if i not in haha:
                haha[i] = 0
            haha[i] += 1
            if haha[i] >= len(nums) / 2:
                return i

if __name__ == '__main__':
    print(Solution().majorityElement([3,2,3]))
    print(Solution().majorityElement([2,2,1,1,1,2,2]))