#encoding:utf8
__author__ = 'gold'

'''
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution1:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        results = []
        if n < 1:
            return results

        def digui(n):
            if n == 1:
                return ['(',')']
            haha = digui(n - 1)
            temp = []
            for h in haha:
                temp.append('(' + h)
                temp.append(')' + h)
            return temp

        temp = digui(n * 2)

        for t in temp:
            if self.valid(t):
                results.append(t)
        return results

    def valid(self,s):
        stack = []
        left = '('
        right = ')'

        for par in s:
            if par == left:
                stack.append(par)
            else:
                if stack and stack[-1] == left:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        helper = []
        self.dfs(helper,ans,0,0,n)
        return ans

    def dfs(self,curList,ans,left,right,n):
        if right > left:
            return
        if left > n:
            return

        if((left == right) and (right == n)):
            ans.append(''.join(curList))
            return
        else:
            if left < n:
                curList.append('(')
                self.dfs(curList,ans,left + 1,right,n)
                curList.pop(-1)
            if right < left:
                curList.append(')')
                self.dfs(curList,ans,left,right + 1,n)
                curList.pop(-1)

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(0))
    print(Solution1().generateParenthesis(3))