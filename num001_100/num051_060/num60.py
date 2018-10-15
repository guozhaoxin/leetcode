#encoding:utf8
__author__ = 'gold'

'''
Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''


import time

class Haha:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums or len(nums) == 1:
            return

        index = len(nums) - 1
        while index > 0:
            if nums[index] > nums[index - 1]:
                lastIndex = len(nums) - 1
                while lastIndex >= index:
                    if nums[lastIndex] > nums[index - 1]:
                        break
                    lastIndex -= 1
                nums[index-1],nums[lastIndex] = nums[lastIndex],nums[index-1]
                self.resort(index,nums)
                return
            else:
                index -= 1

        if index == 0:
            self.resort(0,nums)

    def resort(self,startIndex,nums):
        mid = startIndex + ((len(nums)) - startIndex) // 2
        newL = int(2 * (startIndex + (len(nums) - startIndex - 1) / 2 ))
        index = startIndex
        while index < mid:
            temp = newL - index
            nums[index],nums[temp] = nums[temp],nums[index]
            index += 1

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = []
        for i in range(n):
            nums.append(i + 1)

        haha = Haha()
        count = 1
        while count < k:
            haha.nextPermutation(nums)
            count += 1

        nums = [str(i) for i in nums]
        return ''.join(nums)

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1] * n
        for i in range(1,n):
            fac[i] = fac[i - 1] * i

        nums = [str(i) for i in range(1,n+1)]
        ans = ''
        k -= 1
        for i in range(n):
            j = k // fac[n - i - 1]
            ans += nums[j]
            nums.remove(nums[j])
            k = k % fac[n - i - 1]
        return ans


if __name__ == '__main__':
    print(Solution().getPermutation(4,18))