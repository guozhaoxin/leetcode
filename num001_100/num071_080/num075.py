#encoding:utf8
__author__ = 'gold'

'''
Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

'''


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        left = 0
        while left < len(nums) and nums[left] == 0:
            left += 1
        if left == len(nums):
            return
        right = len(nums) - 1
        while right > -1 and nums[right] == 2:
            right -= 1
        if right == -1:
            return

        index = left + 1

        while index < right:
            if nums[index] == 0:
                nums[left],nums[index] = nums[index],nums[left]
                while left < index:
                    if nums[left] == 0:
                        left += 1
                    else:
                        break
                if left == index:
                    index = left + 1

            elif nums[index] == 2:
                nums[right],nums[index] = nums[index],nums[right]
                while right > index:
                    if nums[right] == 2:
                        right -=1
                    else:
                        break
            else:
                index += 1

        if right == index:
            if nums[index] < nums[left]:
                nums[index],nums[left] = nums[left],nums[index]

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[i] = 1
                i += 1
            if v == 0:
                nums[j] = 0
                j += 1

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) -1
        index = left

        while index <= right:
            if nums[index] < 1:
                nums[left],nums[index] = nums[index],nums[left]
                index += 1
                left += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[right],nums[index] = nums[index],nums[right]
                right -= 1

if __name__ == '__main__':
    import random
    for i in range(1000):
        nums = []
        for i in range(50):
            nums.append(random.randrange(0,3))
        Solution().sortColors(nums)
        for i in range(1,len(nums) - 1):
            if nums[i] < nums[i - 1]:
                print(nums)
                break
        else:
            pass
            # print(True)