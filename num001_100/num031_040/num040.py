#encoding:utf8
__author__ = 'gold'

'''
Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        r = []
        candidates.sort()
        def helper(s,nums,ind):
            if s == 0:
                r.append(nums)
            else:
                for i in range(ind, len(candidates)):
                    num = candidates[i]
                    if i > ind and candidates[i - 1] == num:
                        continue
                    elif s >= num:
                        helper(s - num, nums + [num], i + 1)
                    else:
                        break
        helper(target, [], 0)
        return r

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates,target))