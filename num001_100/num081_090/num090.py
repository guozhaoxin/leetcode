#encoding:utf8
__author__ = 'gold'

'''
Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        if not nums:
            return results

        nums.sort()
        def dfs(index,subList):
            if index == len(nums):
                results.append(subList)
                return
            if index > 0 and nums[index] == nums[index - 1]:
                if not subList:
                    dfs(index + 1,subList + [nums[index]])
                    dfs(index + 1,subList)
                else:
                    if subList[-1] == nums[index]:
                        dfs(index + 1,subList + [nums[index]])
                    else:
                        dfs(index + 1, subList + [nums[index]])
                        dfs(index + 1,subList)
            else:
                dfs(index + 1,subList)
                dfs(index + 1,subList + [nums[index]])

        dfs(0,[])
        return results

if __name__ == '__main__':
    results = Solution().subsetsWithDup([1,2,2])
    print(results)
    print(len(results))