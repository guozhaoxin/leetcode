#encoding:utf8
__author__ = 'gold'

'''
611. Valid Triangle Number

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
'''


class Solution1:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) < 3:
            return 0

        # nums.sort()
        index = 0
        while index < len(nums) and nums[index] == 0:
            index += 1
        if index == len(nums):
            return 0

        count = 0
        for left in range(index,len(nums) - 2):
            for mid in range(left + 1,len(nums) - 1):
                for right in range(mid + 1,len(nums)):
                    if nums[left] + nums[mid] > nums[right]:
                        count += 1
                    else:
                        break

        return count


class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) < 3:
            return 0

        nums.sort()
        i = 0
        while i < len(nums) and nums[i] == 0:
            i += 1
        if i == len(nums):
            return 0

        count = 0
        tempDict = {}
        for i in range(0,len(nums) - 2):
            start = i + 1 if i not in tempDict else tempDict[i]
            for j in range(start,len(nums) - 1):
                k = j + 1
                while k < len(nums):
                    if nums[i] + nums[j] > nums[k]:
                        k += 1
                    else:
                        tempDict[j] = k
                        break
                count += k - j
        print(tempDict)
        return count

if __name__ == '__main__':
    numList = []
    import random
    for i in range(10):
        numList.append(random.randint(0,20))
    numList.sort()
    import time
    start = time.time()
    print(Solution1().triangleNumber(numList))
    print(time.time() - start)
    start = time.time()
    print(Solution().triangleNumber(numList))
    print(time.time() - start)