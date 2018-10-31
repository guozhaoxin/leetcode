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

# import re
# words = 'study in 山海大学'
# regex_str = ".*?([\u4E00-\u9FA5]+大学)"
# match_obj = re.match(regex_str, words)
# if match_obj:
#     print(match_obj.group(1))

import re
text = "Jonny is a good boy, he is    cool, clever, and so on..."
print (re.findall('\w+',text))