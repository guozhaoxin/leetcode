#encoding:utf8
__author__ = 'gold'

'''
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

Accepted
167,626
Submissions
424,735
'''


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        longestSubse = [0] * len(nums)

        for index in range(len(nums)):
            tempLongest = 0
            for j in range(0,index):
                if nums[index] > nums[j]:
                    tempLongest = max(tempLongest,longestSubse[j])
            longestSubse[index] = tempLongest + 1
        return max(longestSubse)


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return len(nums)
        compare = []

        for i in range(len(nums) - 1, -1, -1):
            if not compare:
                compare.append(nums[i])
            else:
                if nums[i] < compare[-1]:
                    compare.append(nums[i])
                elif nums[i] == compare[-1]:
                    continue
                else:
                    pos = self.find(compare, 0, len(compare) - 1, nums[i])
                    compare[pos] = nums[i]
        print(compare)

        return len(compare)

    def find(self, compare, start, end, num):
        if compare[start] <= num: return start
        if compare[end] >= num: return end
        if start + 1 == end or start == end:
            return end
        m = (start + end) // 2
        if num == compare[m]:
            return m
        elif num < compare[m]:
            return self.find(compare, m, end, num)
        else:
            return self.find(compare, start, m, num)


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        subStack = [nums[-1]] #先把最后一个塞进去，省的后边判断来判断去
        for index in range(len((nums)) - 2 ,-1,-1):
            if nums[index] < subStack[-1]:
                subStack.append(nums[index])
            elif nums[index] == subStack[-1]:
                continue
            else:
                position = self.findPosition(nums,subStack,0,len(subStack) - 1,nums[index])
                subStack[position] = nums[index]

        return len(subStack)



    def findPosition(self,nums,subStack,start,end,num):
        '''
        找到num在subStack中应该处于的位置，并返回那个索引
        :param nums:[int,] ,原始的数列
        :param subStack: [int,],到目前为止已经构造好的降序数列栈
        :param start: int,开始索引
        :param end: int,终止索引
        :param num: int,新的要加进来的数字
        :return: int，表示实际应该插入的位置
        '''
        if subStack[start] <= num:
            return start
        if subStack[end] >= num:
            return end
        if start == end or start + 1 == end:
            return end
        mid = (start + end) // 2
        if num == subStack[mid]:
            return mid
        elif num < subStack[mid]:
            return self.findPosition(nums,subStack,mid,end,num)
        else:
            return self.findPosition(nums,subStack,start,mid,num)



if __name__ == '__main__':
    print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))