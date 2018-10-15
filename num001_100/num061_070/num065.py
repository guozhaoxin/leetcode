#encoding:utf8
__author__ = 'gold'

'''
Valid Number

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.


'''


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.strip() #先干掉两边倒空格
        if not s:
            return False

        dotFlag = 0 #标记是否出现了小数点
        eFlag = 0 #标记是否已经出现了科学技术法


        if len(s) == 1 and not s[0].isdigit():
            return False
        nonZero = 0 #标记在e出现前是否已经有了有效的数字

        index = 0
        while index < len(s):
            if s[index].isdigit():
                nonZero = 1
            elif s[index] == '.':
                if index == 0:
                    dotFlag = 1
                elif dotFlag == 1:
                    return False
                elif index == len(s) - 1 and (s[index - 1] == 'e' or s[index - 1] == '+' or s[index - 1] == '-'):
                    return False
                elif eFlag == 1:
                    return False
                else:
                    dotFlag = 1
            elif s[index] == '+' or s[index] == '-':
                if (index != 0) and (s[index - 1 ]!= 'e'):
                    return False
                if index == len(s) - 1:
                    return False
            elif s[index] == 'e':
                if eFlag == 1:
                    return False
                elif not nonZero:
                    return False
                elif index == len(s) - 1:
                    return False
                else:
                    eFlag = 1
            else:
                return False

            index += 1
        return True



class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        try:
            float(s)
            return True
        except Exception as e:
            return False


if __name__ == '__main__':
    print(Solution().isNumber('0'))
    print(Solution().isNumber("0.1"))
    print(Solution().isNumber('abc'))
    print(Solution().isNumber('1 a'))
    print(Solution().isNumber('2e10'))
    print(Solution().isNumber('0..'))
    print(Solution().isNumber('0e1'))
    print(Solution().isNumber('-.'))