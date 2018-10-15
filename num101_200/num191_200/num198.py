#encoding:utf8
__author__ = 'gold'

'''
House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=0
        l=len(nums)
        if l<3:
            for i in nums:
                if i>t:
                    t=i
            return t
        else:
            b=nums
            b.insert(0,0)
            for i in range(3,l+1):
                b[i]=nums[i]+max(b[i-2],b[i-3])
            return max(b[l],b[l-1])


class Solution:
     def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0

        for i in nums:
            last, now = now, max(last + i, now)

        return now


class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)

        res = [0] * 2
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        # res[0], res[1] = nums[0], nums[1]

        for i in range(2, len(nums)):
            res[i % 2] = max(res[(i - 1) % 2], res[(i - 2) % 2] + nums[i])

        return max(res[0], res[1])

if __name__ == '__main__':
    nums = [7, 2, 1, 3, 1]
    # nums = [1,2,3,1]
    # nums = [2,3,2]
    # nums = [1,2]
    print(nums)
    print(Solution().rob(nums))