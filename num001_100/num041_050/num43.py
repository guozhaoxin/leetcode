#encoding:utf8
__author__ = 'gold'

'''
Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        str2num = {
            '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0
        }
        num2str = {
            1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',0:'0'
        }
        if len(num1) == 1 and num1[0] == '0':
            return '0'
        if len(num2) == 1 and num2[0] == '0':
            return '0'

        results = ''
        indexNu1 = len(num1) - 1
        while indexNu1 >= 0:
            indexNu2 = len(num2) - 1
            jinwei = 0
            temp = '0' * (len(num1) - indexNu1 - 1) #先看看要补几个0
            while indexNu2 >= 0:
                mul = str2num[num1[indexNu1]] * str2num[num2[indexNu2]] + jinwei
                cur = mul % 10
                jinwei = mul //10
                temp += num2str[cur]
                indexNu2 -= 1
            if jinwei != 0:
                temp += num2str[jinwei]
            results = self.add(results,temp,str2num,num2str)
            indexNu1 -= 1

        return results[::-1]

    def add(self,num1,num2,str2num,num2str):
        if not num1:
            return num2
        index = 0
        jinwei = 0
        sum = ''
        while index < len(num2) and index < len(num1):
            curSum = str2num[num1[index]] + str2num[num2[index]] + jinwei
            sum += num2str[curSum % 10]
            jinwei = curSum // 10
            index += 1
        while index < len(num1):
            curSum = str2num[num1[index]] + jinwei
            sum += num2str[curSum % 10]
            jinwei = curSum // 10
            index += 1
        while index < len(num2):
            curSum = str2num[num2[index]] + jinwei
            sum += num2str[curSum % 10]
            jinwei = curSum // 10
            index += 1
        if jinwei != 0:
            sum += num2str[jinwei]
        return sum

if __name__ == '__main__':
    import random
    s = Solution()
    f = open('results.txt','w')
    for i in range(10000):
        a = random.randint(0,10000)
        b = random.randint(0,10000)
        mul = a * b
        res = s.multiply(str(a),str(b))
        mul = str(mul)
        if mul == res:
            content = str(a) + ' ' + str(b) + ' ' + str(mul) + ' ' + str(True)
            print(content)
            f.write(content + '\n')
        else:
            content = str(a) + ' ' + str(b) + ' ' + str(mul) + ' '  + str(res) + ' '+ str(True)
            print(content)
            f.write(content + '\n')
    f.close()