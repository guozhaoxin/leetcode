#encoding:utf8
__author__ = 'gold'

# from functools import reduce
# a =reduce(lambda x,y:x + y,set([1,2,3]),10)
# print(a)
# a = reduce(lambda x, y: x * y, range(9, -1, -1), 9)
# print(a)

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(s='',left=0,right=0):
            if len(s) == 2 * n:
                ans.append(s)
            if left < n:
                backtrack(s + '(',left + 1,right,)
            if right < left:
                backtrack(s + ')',left,right + 1)

        backtrack()

        return ans

