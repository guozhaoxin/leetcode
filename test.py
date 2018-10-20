#encoding:utf8
__author__ = 'gold'

b = ['1df','bx','cy']

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        ["flower","flow","flight"]
        """
        if not strs:
            return ""

        for x in zip(*strs):
            print(x)

        print('****')

        for x,y in enumerate(zip(*strs)):
            print(x,y)

        for i,ch in enumerate(zip(*strs)):
            if len(set(ch)) != 1:
                return strs[0][:i]
        else:
            return min(strs,key = len)

results ={}
for i in range(60):
    binnum = bin(i)[2:]
    count1 = binnum.count('1')
    if count1 not in results:
        results[count1] = []
    results[count1].append(str(int(binnum,base=2)))
print(results)