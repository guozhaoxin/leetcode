#encoding:utf8
__author__ = 'gold'

'''
338. Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        dpDict = {}
        res.append(0)
        dpDict[0] = 1
        left = 0
        right = 1
        for num in range(1,num + 1):
            if num == left:
                res.append(1)
                dpDict[num] = 1
            elif num == right:
                res.append(1)
                dpDict[num] = 1
                left = right
                right <<= 1
            else:
                count = dpDict[left] + dpDict[num - left]
                res.append(count)
                dpDict[num] = count

        return res

if __name__ == '__main__':
    print(Solution().countBits(0))
    print(Solution().countBits(1))
    print(Solution().countBits(15))