#encoding:utf8
__author__ = 'gold'

'''
213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            try:
                return max(nums)
            except Exception as e:
                return 0

        res1 = [0] * 2
        res1[0],res1[1] = nums[0],max(nums[0],nums[1])
        # for i in range(2,len(nums) - 1):
        #     res1[i % 2] = max(res1[(i - 2) % 2] + nums[i],res1[(i - 1) % 2])

        res2 = [0] * 2
        res2[0], res2[1] = nums[1], max(nums[1], nums[2])
        # for i in range(3, len(nums)):
        #     res2[(i - 1) % 2] = max(res2[(i - 3) % 2] + nums[i], res2[(i - 2) % 2])

        for i in range(2,len(nums) - 1):
            res1[i % 2] = max(res1[(i - 2) % 2] + nums[i], res1[(i - 1) % 2])
            res2[i % 2] = max(res2[(i - 2) % 2] + nums[i + 1],res2[(i - 1) % 2])

        return max(max(res1),max(res2))


class Solution1:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            try:
                return max(nums)
            except Exception as e:
                return 0

        res1 = [0] * (len(nums) - 1)
        res1[0],res1[1] = nums[0],max(nums[0],nums[1])
        res2 = [0] * (len(nums) - 1)
        res2[0],res2[1] = nums[1],max(nums[1],nums[2])

        for i in range(2,len(nums) - 1):
            res1[i] = max(res1[i - 2] + nums[i],res1[i - 1])

        for i in range(3,len(nums)):
            res2[i - 1] = max(res2[i - 3] + nums[i],res2[i - 2])

        return max(max(res2),max(res1))

if __name__ == '__main__':
    print(Solution().rob([]))
    print(Solution().rob([1,2]))
    print(Solution().rob([1,2,1]))
    print(Solution().rob([1,2,3,1]))
    print(Solution().rob([1,2,3,1,3]))
    print(Solution().rob([1,2,3,1,3]))