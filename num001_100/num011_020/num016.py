#encoding:utf8
__author__ = 'gold'

'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution_:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #先处理特殊情况
        if len(nums) <= 2:
            return None
        if len(nums) == 3:
            return sum(nums)

        #先排序吧还是
        nums.sort()

        nearestSum = nums[0] + nums[1] + nums[-1] #代表最小和
        smallGap = abs(nearestSum - target) #表示最小差距

        leftIndex = 0 #表示左边的索引
        rightIndex = len(nums) - 1 #表示右边的索引

        while leftIndex < rightIndex - 1: #要求左边的索引不能超过右边数字前一个的索引，保证至少有三个数
            lastGap = None #表示上一个差距，用来与当前这个对比，看是不是一直在接近
            for middleIndex in range(leftIndex + 1,rightIndex):
                tempSum = nums[leftIndex] + nums[rightIndex] + nums[middleIndex]
                gap = abs(tempSum - target)
                if gap < smallGap: #找到一个符合的
                    smallGap = gap
                    nearestSum = tempSum
                if gap == 0:#倘若找到一个差为0的，则不可能找到比它更接近的了，直接返回
                    return target
                if lastGap is None:
                    lastGap = gap
                else:
                    if lastGap < gap: #表示和当前left和right下，它们能达到的和已经最接近了，没必要再继续选了
                        break
                    else:
                        lastGap = gap
            if nums[leftIndex] + nums[rightIndex] < target:#说明当前索引下两个数的和小于target，需要左边往右边跳
                leftIndex += 1
            elif nums[leftIndex] + nums[rightIndex] > target:
                rightIndex -= 1
            else:
                #这个时候需要考虑最接近的和会怎么样
                if nearestSum < target:
                    leftIndex += 1
                else:
                    rightIndex -= 1
        return nearestSum

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) <= 3:
            return sum(nums)

        nums.sort()
        nearest = None
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tempSum = nums[i] + nums[left] + nums[right]
                if tempSum == target:
                    return target
                current_diff = abs(tempSum - target)
                if nearest != None:
                    nearest_diff = abs(nearest - target)
                    if nearest_diff > current_diff:
                        nearest = tempSum
                else:
                    nearest = tempSum
                if tempSum < target:
                    left += 1
                else:
                    right -= 1
        return nearest

if __name__ == '__main__':
    nums = [0,2,1,-3]
    print(Solution().threeSumClosest(nums,1))