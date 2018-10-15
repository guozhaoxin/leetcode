#encoding:utf8
__author__ = 'gold'

'''
Longngest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        numSet = set(nums)

        longest = 0
        for num in nums:
            if num - 1 in numSet:
                continue
            curN = num + 1
            while curN in numSet:
                curN += 1
            longest = max(longest,curN - num)
        return longest

if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(Solution().longestConsecutive([1,0,-1]))