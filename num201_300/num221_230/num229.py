#encoding:utf8
__author__ = 'gold'

'''
Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        results = []
        nums.sort()

        left = 0
        lengthen = len(nums) // 3 + 1
        while left < len(nums) and len(results) < 2:
            right = left + lengthen - 1
            if right >= len(nums):
                break
            if nums[left] == nums[right]:
                results.append(nums[left])
                while right < len(nums):
                    if nums[right] != nums[left]:
                        break
                    right += 1
                left = right
            else:
                left += 1

        return results

if __name__ == '__main__':
    print(Solution().majorityElement([3,2,3]))
    print(Solution().majorityElement([1,1,1,3,3,2,2,2]))