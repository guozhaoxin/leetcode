#encoding:utf8
__author__ = 'gold'

'''
313.
Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        if n <= 1:
            return 1

        primeList = [1]
        indexList = [0 for i in range(len(primes))]
        productList = [factor for factor in primes]

        while len(primeList) < n:
            smallIndex = 0
            for index in range(1,len(productList)):
                if productList[index] < productList[smallIndex]:
                    smallIndex = index
            if productList[smallIndex] > primeList[-1]:
                primeList.append(productList[smallIndex])
            indexList[smallIndex] += 1
            productList[smallIndex] = primeList[indexList[smallIndex]] * primes[smallIndex]
        return primeList[-1]


if __name__ == '__main__':
    print(Solution().nthSuperUglyNumber(2,[2,7,13,19]))
    print(Solution().nthSuperUglyNumber(10,[2,5,7,11,13,17,23,29,43,53]))