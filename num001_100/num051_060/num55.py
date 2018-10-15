#encoding:utf8
__author__ = 'gold'

'''
Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        if len(nums) == 1:
            return True

        if nums[0] >= len(nums):
            return True

        results = [0 for i in range(len(nums))]
        results[-1] = 1

        index = len(nums) - 1

        while index >= 0:
            maxStep = nums[index]
            curMaxPos = index + maxStep
            if curMaxPos >= len(nums) - 1:
                results[index] = 1
            else:
                for step in range(1,maxStep + 1):
                    if results[index + step] == 1:
                        results[index] = 1
                        break
            index -= 1

        return True if results[0] else False

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        if len(nums) == 1:
            return True

        if nums[0] >= len(nums):
            return True

        if nums[0] == 0:
            return False

        results = [0 for i in range(len(nums))]
        results[-1] = 1

        index = len(nums) - 1

        while index >= 0:
            maxStep = nums[index]
            curMaxPos = index + maxStep
            if curMaxPos >= len(nums) - 1:
                results[index] = 1
            else:
                for step in range(maxStep,0,-1):
                    if results[index + step] == 1:
                        results[index] = 1
                        break

            if results[index] and nums[0] >= index:
                results[0] = 1
                break

            index -= 1

        return True if results[0] else False


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        if len(nums) == 1:
            return True

        if nums[0] >= len(nums):
            return True

        if nums[0] == 0:
            return False

        index = len(nums) - 2
        lastPos = len(nums) - 1
        while index >= 0:
            if nums[index] + index >= lastPos:
                lastPos = index
            index -= 1

        if lastPos == 0:
            return True
        return False

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    nums = [3, 2, 1, 0, 4]
    print(Solution().canJump(nums))