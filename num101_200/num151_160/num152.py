#encoding:utf8
__author__ = 'gold'

'''
Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        assert len(nums)

        maxPro = nums[0]

        index = 0
        while index < len(nums):
            maxPro = max(maxPro,nums[index])
            while index < len(nums) and nums[index] == 0:
                index += 1
            if index == len(nums):
                break

            if nums[index] < 0 and (index == len(nums) - 1 or (nums[index + 1] == 0)):
                maxPro = max(maxPro,nums[index])
                index += 1
                continue
            product = nums[index]
            tempPro = [] if nums[index] > 0 else [(index, nums[index])]
            index += 1
            while index < len(nums) and nums[index] != 0:
                if nums[index] < 0:
                    tempPro.append((index,product * nums[index]))
                    product = tempPro[-1][1]
                else:
                    product *= nums[index]
                maxPro = max(maxPro,product)
                index += 1
            if product < 0:
                if len(tempPro) == 1:
                    left = tempPro[0][1] // nums[tempPro[0][0]]
                    right = product // tempPro[0][1]
                    maxPro = max(maxPro,left,right)
                else:
                    right = tempPro[-1][1] // nums[tempPro[-1][0]]
                    left = product // tempPro[0][1]
                    maxPro = max(maxPro,left,right)
            else:
                maxPro = max(maxPro,product)

        return maxPro



class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # also need to remember the smallest result
        big = small = res = nums[0]
        for num in nums[1:]:
            big, small = max(num, big * num, small * num), min(num, big * num, small * num)
            print(big,small)
            res = max(big, res)
        return res


if __name__ == '__main__':
    print(Solution().maxProduct([2,3,-2,4]))
    # print(Solution().maxProduct([1,2,0,-1,-2,3,-8,-7,6,-10]))
    # print(Solution().maxProduct([-2,0,-1]))