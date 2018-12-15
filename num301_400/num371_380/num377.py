#encoding:utf8
__author__ = 'gold'

'''
377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
'''

'''
there are at least 4 ways to reach the goal,but the basic idea is the same:
to get the target,we can scan the array:
    if the num is larger than the target,then we cann't the result through nu;
    if the num is not larger than the target,then we can check if target - num is in the array. 
'''


class Solution1:
    def combinationSum4(self, nums, target):
        """
        the brute force recursion,for every num ,we check if we can get a goal lits through it,and never
        save any  intermediary result;
        Time Limit Exceeded
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target == 0:
            return 1

        res = 0
        for num in nums:
            if num <= target:
                res += self.combinationSum4(nums,target - num)
        return res


class Solution2:
    def combinationSum4(self, nums, target):
        """
        save the intermediary result,we can struct a array which has target + 1 elements,
        all element is -1 in the array,while the first element is 1;
        from index is 1 on,we calculate if cur index can be reached through every num in the nums array,
        that means if index is not smaller than num and index - num in the nums(if not ,then tempList[index-] - num) is 0

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tempList = [-1] * (target + 1)
        tempList[0] = 1
        result = self.__helper(target,nums,tempList)
        return result

    def __helper(self,target,nums,tempList):
        if tempList[target] != -1:
            return tempList[target]

        res = 0
        for num in nums:
            if num <= target:
                res += self.__helper(target - num,nums,tempList)
        tempList[target] = res
        return res

class Solution4:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tempList = [0] * (target + 1)
        tempList[0] = 1

        for i in range(1,len(tempList)):
            for index in range(len(nums)):
                if i >= nums[index]:
                    tempList[i] += tempList[i - nums[index]]
        return tempList[-1]

class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dpDic = {0:1}
        return self.__helper(target,dpDic,nums)

    def __helper(self,target,dpDic,nums):
        if target in dpDic:
            return dpDic[target]

        res = 0
        for num in nums:
            if num <= target:
                res += self.__helper(target - num,dpDic,nums)
        dpDic[target] = res

        return dpDic[target]

if __name__ == '__main__':
    # print(Solution().combinationSum4([4,2,1],32))
    # print(Solution().combinationSum4([3,2,1],4))
    # print(Solution().combinationSum4([3,4,5,6],100))
    print(Solution() .combinationSum4([3,4,5,6],7))