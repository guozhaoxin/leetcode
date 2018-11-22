#encoding:utf8
__author__ = 'gold'

'''
713. Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0

        start = 0
        end = -1
        product = 1

        while start < len(nums):
            if end < start:
                end = start
            else:
                end += 1
            while end < len(nums):
                product *= nums[end]
                if product >= k:
                    product //= nums[end]
                    end -= 1
                    break
                end += 1
            if end == len(nums):
                count += (end - start) * (end - start + 1) // 2
                break
            if start > end:
                start += 1
                continue
            count += end - start + 1
            product //= nums[start]
            start += 1


        return count

if __name__ == '__main__':
    print(Solution().numSubarrayProductLessThanK([10,5,2,6],100))
    print(Solution().numSubarrayProductLessThanK([100,100,100],100))