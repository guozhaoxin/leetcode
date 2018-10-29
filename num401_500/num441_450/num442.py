# coding:utf8
__author__ = 'gold'

'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?


Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

'''


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                results.append(index + 1)
            else:
                nums[index] = -nums[index]

        return results

if __name__ == '__main__':
    print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))