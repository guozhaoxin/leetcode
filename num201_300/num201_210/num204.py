#encoding:utf8
__author__ = 'gold'

'''
Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        priList = [2]

        for i in range(3,n):
            print(i)
            result = True
            for primr in priList:
                if primr * primr > i:
                    break
                if i % primr == 0:
                    result = False
                    break
            if result:
                priList.append(i)


        return len(priList)


class Solution:
# @param {integer} n
# @return {integer}
    def countPrimes(self, n):
        if n < 2:
            return 0
        if n == 3:
            return 1
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

if __name__ == '__main__':
    print(Solution().countPrimes(1000000))