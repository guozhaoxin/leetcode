#encoding:utf8
__author__ = 'gold'

'''
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
'''


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        coins.sort() #先排序
        self.tempResultDic = {}
        return self.__helper(coins,amount)

    def __helper(self,coins,amount):
        print(amount)
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in self.tempResultDic:
            return self.tempResultDic[amount]
        temp = []
        for coin in coins:
            if coin <= amount:
                if amount % coin == 0:
                    temp.append(amount // coin)
                    continue
                result = self.__helper(coins,amount - coin)
                if result >= 0:
                    temp.append(result + 1)
            else:
                break
        if not temp:
            return -1
        self.tempResultDic[amount] = min(temp)
        return self.tempResultDic[amount]


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [amount + 1] * (amount + 1)
        table[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    table[i] = min(table[i], table[i - coin] + 1)
        if table[amount] > amount:
            return -1
        else:
            return table[amount]


class Solution1:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        def dfs(amount, count, start):
            if count - (-amount // coins[start]) >= result[0]: return
            if amount % coins[start] == 0:
                result[0] = min(result[0], count + amount // coins[start])
                return
            if start == n - 1: return
            for i in range(amount // coins[start], -1, -1):
                dfs(amount - i * coins[start], count + i, start + 1)

        if not coins: return -1
        n = len(coins)
        max_val = amount + 1
        result = [max_val]
        coins.sort(reverse=True)
        dfs(amount, 0, 0)
        print(result)
        return result[0] if result[0] < max_val else -1


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        if not amount:
            return 0
        coins.sort(reverse = True)
        self.maxVal = amount + 1
        self.coins = coins
        self.__helper(amount,0,0)

        if self.maxVal > amount:
            return -1
        return self.maxVal

    def __helper(self,amount,index,count):
        if amount == 0:
            return
        if count + amount // self.coins[index] > self.maxVal:
            return
        if amount % self.coins[index] == 0:
            self.maxVal = min(self.maxVal,count + amount // self.coins[index])
            return
        if index == len(self.coins) - 1:
            return
        for i in range(amount // self.coins[index],-1,-1):
            self.__helper(amount - i * self.coins[index],index + 1,count + i)

if __name__ == '__main__':
    # print(Solution().coinChange([1,2,5],18))
    # print(Solution().coinChange([2],3))
    print(Solution().coinChange([186,419,83,408],6249))
    print(Solution().coinChange([1,2,5],1000))
    print(Solution().coinChange([71,440,63,321,461,310,467,456,361],9298))
    print(Solution1().coinChange([71,440,63,321,461,310,467,456,361],9298))