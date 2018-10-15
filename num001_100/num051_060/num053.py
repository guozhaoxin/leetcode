#encoding:utf8
__author__ = 'gold'

'''
 Maximum Subarray
 
 Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        1、排除了特殊情况（空数组，或数组只有一个元素）
        2、从第0个元素开始，先假设其为最大子序列和
        3、从第1个元素开始，首先判断这个元素，如果它大于0，则要根据到目前为止这段子序列的和情况看：
            3.1）如果目前的这段子序列（不包括当前元素）大于0，则可以将当前元素加上去并判断是否超过目前得到的最大和
            3.2）如果目前这段子序列小于0，则可以将当前元素设置为新的子序列的开始，并更新目前子序列的和
        4、如果当前元素小于0，而目前子序列和大于0，则可以将当前元素加入子序列
        5、如果当前元素小于0，而目前子序列也小于0，则将当前元素设置为新子序列的头元素
        """

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        maxSum = nums[0]
        curSum = maxSum
        index = 1
        while index < len(nums):
            if nums[index] < 0 and curSum < 0:
                curSum = nums[index]
            elif curSum < 0 and nums[index] >= 0:
                curSum = nums[index]
            else:
                curSum += nums[index]

            if maxSum < curSum:
                maxSum = curSum
            index += 1
        return maxSum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [0,0,0,1,-1,2,4]
    print(Solution().maxSubArray(nums))