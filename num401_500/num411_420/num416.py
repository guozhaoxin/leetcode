#encoding:utf8
__author__ = 'gold'

'''
416. Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False

        totalSum = sum(nums)
        half = totalSum // 2
        if half * 2 != totalSum:
            return False

        nums.sort(reverse = True)
        if half < nums[0]:
            return False
        if half == nums[0]:
            return True

        remainder = half - nums[0]
        for index in range(1,len(nums)):
            if remainder < nums[index]:
                continue
            if self.__helper(nums,remainder,index):
                return True

        return False

    def __helper(self,nums,remainder,index):
        if index == len(nums):
            return False

        if remainder == nums[index]:
            return True

        if remainder < nums[index]:
            return False

        result = False
        remainder -= nums[index]
        for j in range(index + 1,len(nums)):
            if remainder == nums[j]:
                return True
            if remainder < nums[j]:
                continue
            result = self.__helper(nums,remainder - nums[j],j + 1)
            if result:
                break

        return result


if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 11, 5]))
    print(Solution().canPartition([1, 2, 3, 5]))
    print(Solution().canPartition([3,3,3,4,5]))
    print(Solution().canPartition([1,3,4,4]))
    print(Solution().canPartition([99,2,3,98]))