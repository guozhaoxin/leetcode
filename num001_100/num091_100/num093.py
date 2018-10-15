#encoding:utf8
__author__ = 'gold'

'''
Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        if not s:
            return results

        def dfs(bit,index,subIP):
            if index == len(s) and bit == 5:
                results.append(subIP)
                return
            if index == len(s):
                return
            if bit == 5:
                return
            for i in range(3):
                if index + i >= len(s):
                    break
                try:
                    curByte = int(s[index:index + i + 1])
                except Exception as e:
                    curByte = -1
                if curByte > 0 and curByte <= 255 and not s[index:index + i + 1].startswith('0') or curByte == 0 and i == 0:
                    if not subIP:
                        newSubIP = s[index:index + i + 1]
                    else:
                        newSubIP = subIP + '.' + s[index:index + i + 1]
                    dfs(bit + 1,index + i + 1,newSubIP)

        dfs(1,0,'')
        return results

if __name__ == '__main__':
    input = "25525511135"
    input = "010010"
    output = Solution().restoreIpAddresses(input)
    print(output)