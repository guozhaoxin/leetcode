#encoding:utf8
__author__ = 'gold'

'''
Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack = [] #保留数字？
        opeStack = [] #保留所有符号
        index = 0
        needNum = True
        while index < len(s):
            if s[index] == ' ':
                index += 1
            else:
                if s[index].isdigit():
                    right = index + 1
                    while right < len(s) and s[right].isdigit():
                        right += 1
                    num = int(s[index:right])
                    if needNum:
                        needNum = False
                    if opeStack and opeStack[-1] != '(':
                        num1 = stack.pop()
                        stack.append(self.cal(num1,num,opeStack.pop()))
                    else:
                        stack.append(num)
                    index = right
                elif s[index] == '(':
                    opeStack.append(s[index])
                    needNum = True
                    index += 1
                elif s[index] == '+' or s[index] == '-':
                    if needNum == True:
                        stack.append(0)
                        needNum = False
                    opeStack.append(s[index])
                    index += 1
                else:
                    opeStack.pop()
                    if opeStack and (opeStack[-1] == '+' or opeStack[-1] == '-'):
                        num2 = stack.pop()
                        num1 = stack.pop()
                        num = self.cal(num1,num2,opeStack.pop())
                        stack.append(num)
                    index += 1
        return stack[-1]


    def cal(self,a,b,cal):
        if cal == '+':
            return a + b
        return a - b


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

        sign = 1
        val = 0
        curr = 0
        stack = []

        for c in s:
            if c in digits:
                curr = curr * 10 + int(c)
            elif c == '+':
                val = val + sign * curr
                curr = 0
                sign = 1
            elif c == '-':
                val = val + sign * curr
                curr = 0
                sign = -1
            elif c == '(':
                stack.append(val)
                stack.append(sign)
                sign = 1
                val = 0
            elif c == ')':
                val = val + sign * curr
                curr = 0
                val = val * stack.pop()
                val = val + stack.pop()

        if curr != 0:
            val += curr * sign
        return val

if __name__ == '__main__':
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
    print(Solution().calculate( " 2-1 + 2 "))
    print(Solution().calculate( " 1+ 1"))
    print(Solution().calculate( " -1+ 1"))