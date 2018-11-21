#encoding:utf8
__author__ = 'gold'

'''
556. Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21

 

Example 2:

Input: 21
Output: -1

#fuck this code
'''


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        numStr = str(n)
        index = len(numStr) - 1
        while index > 0:
            if numStr[index - 1] < numStr[index]:
                result = numStr[:index - 1]
                splitIndex = len(numStr) - 1

                while splitIndex > index:
                    if numStr[index - 1] < numStr[splitIndex] <= numStr[index]:
                        break
                    splitIndex -= 1
                result += numStr[splitIndex]
                temp = numStr[index:splitIndex] + numStr[index - 1] + numStr[splitIndex + 1:]
                result += temp[::-1]
                if int(result) >= 2 ** 31 - 1:
                    return -1
                return int(result)

            index -= 1

        return -1

if __name__ == '__main__':
    print(Solution().nextGreaterElement(123))
    print(Solution().nextGreaterElement(1))
    print(Solution().nextGreaterElement(0))
    print(Solution().nextGreaterElement(123456789))
    print(Solution().nextGreaterElement(987654321))
    print(Solution().nextGreaterElement(101))
    print(Solution().nextGreaterElement(110))
    print(Solution().nextGreaterElement(123987654))
    print(Solution().nextGreaterElement(230241))
    print(Solution().nextGreaterElement(12443322))
    print(Solution().nextGreaterElement(12222333))
    print(Solution().nextGreaterElement(12443322))
    print(Solution().nextGreaterElement(2147483647))