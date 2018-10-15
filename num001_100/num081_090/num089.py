#encoding:utf8
__author__ = 'gold'

'''
Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
'''


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        numSet = set()
        for i in range(1,2 ** n):
            numSet.add(i)
        result = ['0' * n]
        strSet = set()
        strSet.add(result[0])
        self.dfs(result,strSet,2 ** n,n)
        for i in range(len(result)):
            result[i] = int(result[i],2)
        return result


    def dfs(self,result,strSet,size,n):
        if len(result) == size:
            return
        for i in range(n):
            temp = result[-1][:i] + str(int(result[-1][i]) ^ 1) + result[-1][i + 1:]
            if temp not in strSet:
                strSet.add(temp)
                result.append(temp)
                self.dfs(result,strSet,size,n)
                if len(result) == size:
                    return
                else:
                    result.pop()
                    strSet.remove(temp)


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        result = [0]
        for i in range(n):
            temp = 2 ** i
            result += [ x + temp for x in reversed(result)]
        return result


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(2 ** n):
            result.append(i ^ (i >> 1))

        return result

if __name__ == '__main__':
    results = Solution().grayCode(2)
    print('????')
    print(results)