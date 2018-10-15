#encoding:utf8
__author__ = 'gold'

'''
Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        if not path:
            return '/'

        results = [] #保存所有文件夹名称
        dicSplit = path.split('/')

        for d in dicSplit:
            if not d or d == '.':
                continue
            if d == '..' and len(results) > 0:
                results.pop()
            elif d != '..':
                results.append(d)
        results = '/' + '/'.join(results)

        return results

if __name__ == '__main__':
    print(Solution().simplifyPath("/../"))