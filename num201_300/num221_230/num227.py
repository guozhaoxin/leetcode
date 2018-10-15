#encoding:utf8
__author__ = 'gold'

'''
Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
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
        operatorPri = {'+':1,'-':1,'*':2,'/':2,'(':3,')':3}

        stack = []
        operStack = []
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            if s[index].isdigit():
                right = index + 1
                while right < len(s) and s[right].isdigit():
                    right += 1
                stack.append(int(s[index:right]))
                index = right
                continue
            else:
                if not operStack:
                    operStack.append(s[index])
                elif s[index] == ')':
                    while operStack and operStack[-1] != '(':
                        stack.append(operStack.pop())
                    if operStack and operStack[-1] == '(':
                        operStack.pop()
                elif operatorPri[s[index]] > operatorPri[operStack[-1]]:
                    operStack.append(s[index])
                else:
                    while operStack and operStack[-1] != '(' and operatorPri[operStack[-1]] >= operatorPri[s[index]]:
                        stack.append(operStack.pop())
                    operStack.append(s[index])
                index += 1
        while operStack and operStack[-1] != '(':
                stack.append(operStack.pop())

        index = 0
        while index < len(stack):
            if isinstance(stack[index],(int,float)):
                index += 1
            else:
                left = index - 1
                while not isinstance(stack[left],(int,float)):
                    left -= 1
                num2 = stack[left]
                # print(num2)
                stack[left] = None
                left -= 1
                while not isinstance(stack[left],(int,float)):
                    left -= 1
                num1 = stack[left]
                stack[left] = None
                ans = self.cal(num1,num2,stack[index])
                stack[index] = ans
                index += 1
        index = len(stack) - 1
        while not isinstance(stack[index],(int,float)):
            index -= 1
        return stack[index]


    def cal(self,num1,num2,oper):
        if oper == '+':
            return num1 + num2
        if oper == '-':
            return num1 - num2
        if oper == '*':
            return num1 * num2
        return num1 // num2


if __name__ == '__main__':
    print(Solution().calculate("3+2*2"))
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
    print(Solution().calculate("(1+2*3 + (4* 5 + 6) * 7"))