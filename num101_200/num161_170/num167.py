#encoding:utf8
__author__ = 'gold'

'''
Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return []

        index = 0
        while index < len(numbers):
            if numbers[index] > target:
                return []

            dif = target - numbers[index]

            left = index + 1
            right = len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == dif:
                    return [index + 1,mid + 1]
                if numbers[mid] < dif:
                    left = mid + 1
                else:
                    right = mid - 1

            index += 1
        return []

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return []
        numDic = dict()

        for index in range(len(numbers)):
            if numbers[index] in numDic:
                numDic[numbers[index]].append(index)
            else:
                numDic[numbers[index]] = [index]

        for num in numbers:
            dif = target - num
            if dif != num and dif in numDic:
                return [numDic[num][0] + 1,numDic[dif][0] + 1]
            if dif == num and len(numDic[num]) >= 2:
                return [numDic[num][0] + 1,numDic[num][1] + 1]
        return []


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = set(numbers)
        n = len(numbers)
        for i in range(n):
            if target - numbers[i] in num:
                j = numbers.index(target-numbers[i])
                if i != j:
                    return [i+1,j+1]
                return [i+1,j+2]


if __name__ == '__main__':
    # numbers = [2, 7, 11, 15]
    # target = 9

    numbers = [3, 4, 5,11, 15]
    target = 6

    print(Solution().twoSum(numbers,target))