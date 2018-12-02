#encoding:utf8
__author__ = 'gold'

'''
306.
Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
Follow up:
How would you handle overflow for very large input integers?
'''

class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num or len(num) <= 2:
            return False

        for i in range(0,len(num) // 2 + 1):
            a = self.str2num(num,0,i + 1)
            if a == -1:
                continue

            for j in range(i + 1,(len(num) - i - 1)//2 + 1 + i):
                b = self.str2num(num,i + 1,j + 1)
                if self.dfs(num,j + 1,a,b,i + 1,j - i):
                    return True

        return False


    def dfs(self,s,index,a,b,aBitCount,bBitCount):
        '''
        对字符串从索引开始的部分判断
        :param s:str，判断的字符串
        :param index:int,新的字符串开始的索引
        :param a:int，第一个加数
        :param b:int，第二个加数
        :param aBitCount:int,a的位数
        :param bBitCount:int,b的位数
        :return:boolean
        '''

        if index == len(s):
            if aBitCount + bBitCount == len(s):
                return False
            return True

        for i in range(2):
            try:
                newBitCount = max(aBitCount,bBitCount)
                nextA = self.str2num(s,index,index + newBitCount + i)
                if nextA == -1:
                    continue
                if a + b != nextA:
                    continue
                a,b = b,nextA
                return self.dfs(s,index + newBitCount + i,a,b,bBitCount,newBitCount + i)
            except Exception as e:
                continue
        return False

    def str2num(self,s,index,end):
        '''
        将一个字符串中的一部分转化为一个整数，
        在这个题目中主要是对非法的数据（本题应该不存在这种情况）以及有前导零的数进行删除
        :param s: str，目标字符串
        :param index: int，子字符串的开始索引
        :param end: int，子字符串的终止索引加1
        :return: int，如果是个有效的子字符串则转化为对应的int，否则返回-1
        '''

        if index >= len(s):
            return -1

        if s[index] == '0' and index < end - 1:
            return -1

        try:
            num = int(s[index:end])
            return num
        except Exception as e:
            return -1

if __name__ == '__main__':
    print(Solution().isAdditiveNumber("112358"))
    print(Solution().isAdditiveNumber("199100199"))
    print(Solution().isAdditiveNumber("0"))
    print(Solution().isAdditiveNumber("1"))
    print(Solution().isAdditiveNumber("10"))
    print(Solution().isAdditiveNumber("1123581321345589144"))
    print(Solution().isAdditiveNumber("581321345589144"))
