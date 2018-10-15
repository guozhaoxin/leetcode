#encoding:utf8
__author__ = 'gold'

'''
Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        results = []

        if not nums:
            return results

        def digui(index,curList):
            if index < len(nums):
                digui(index + 1,curList)
                digui(index + 1,curList + [nums[index]])
            else:
                results.append(curList)

        digui(0,[])
        return results


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return self.subsetHelper([], nums, [])

    def subsetHelper(self, currSet, remaining, sets):
        if remaining == []:
            sets.append(currSet)
        else:
            element = remaining.pop()
            self.subsetHelper(currSet + [element], remaining, sets)
            self.subsetHelper(currSet, remaining, sets)

            remaining.append(element)

        return sets


if __name__ == '__main__':
    nums = [1,2,3,4]
    res = Solution().subsets(nums)
    print(res)
    print(len(res))
    print(nums)