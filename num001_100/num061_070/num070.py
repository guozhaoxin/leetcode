#encoding:utf8
__author__ = 'gold'

'''
Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        tempSteps = [0 for i in range(n)]

        def digui(stairs):
            if stairs == n:
                return 1
            elif stairs > n:
                return 0
            if tempSteps[stairs] > 0:
                return tempSteps[stairs]
            tempSteps[stairs] = digui(stairs + 1) + digui(stairs + 2)
            return tempSteps[stairs]

        return digui(0)

if __name__ == '__main__':
    print(Solution().climbStairs(3))