#encoding:utf8
__author__ = 'gold'

'''
Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        shortestL = len(nums) + 1
        left = 0
        if nums[0] >= s:
            return 1
        sum = nums[0]
        right = 1

        while right < len(nums):
            if nums[right] >= s:
                return 1
            if nums[right] + sum < s:
                sum += nums[right]
            else:
                shortestL = min(shortestL,right - left + 1)
                while left < right:
                    sum -= nums[left]
                    if sum + nums[right] >= s:
                        left += 1
                        shortestL = min(shortestL,right - left + 1)
                    else:
                        sum += nums[left] + nums[right]
                        break
            right += 1

        if sum >= s and shortestL == len(nums) + 1:
            shortestL = len(nums)

        return 0 if shortestL == len(nums) + 1 else shortestL

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        left = 0
        if nums[left] >= s:
            return 1
        curSum = nums[0]
        right = 1
        shortestL = len(nums) + 1

        while right < len(nums):
            if nums[right] >= s:
                return 1
            curSum += nums[right]
            if curSum < s:
                pass
            else:
                shortestL = min(shortestL,right - left + 1)
                while left < right:
                    if curSum >= s:
                        shortestL = min(shortestL,right - left + 1)
                        curSum -= nums[left]
                        left += 1

                    else:
                        left -= 1
                        curSum += nums[left]
                        break
            right += 1
        if curSum >= s and shortestL == len(nums) + 1:
            shortestL = len(nums)

        return 0 if shortestL == len(nums) + 1 else shortestL


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7,[2,3,1,2,4,3]))
    print(Solution().minSubArrayLen(15,[1,3,2,6,5,4,7,10,8]))
    print(Solution().minSubArrayLen(15,[1,2,3,4,5]))
    print(Solution().minSubArrayLen(5,[2,3,1,1,1,1,1]))