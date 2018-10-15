#encoding:utf8
__author__ = 'gold'

'''
Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?


'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]
        s = s[::-1]
        while len(s) < 32:
            s = s + '0'
        print(s)
        num = int(s,base=2)
        return num

if __name__ == '__main__':
    print(Solution().reverseBits(100))