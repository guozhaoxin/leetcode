#encoding:utf8
__author__ = 'gold'

'''
Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        result = []
        if not root:
            return result

        def dfs(node,pathStr):
            if not node.left and not node.right:
                if pathStr:
                    result.append(pathStr + '->' + str(node.val))
                else:
                    result.append(str(node.val))
                return
            if pathStr:
                pathStr = pathStr + '->' + str(node.val)
            else:
                pathStr = str(node.val)
            if node.left:
                dfs(node.left,pathStr)
            if node.right:
                dfs(node.right,pathStr)


        dfs(root,'')
        return result


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        result = []
        if not root:
            return result

        if not root.left and not root.right:
            result.append(str(root.val))
            return result

        def dfs(node,path):
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return
            else:
                path = path + str(node.val) + '->'
                if node.left:
                    dfs(node.left,path)
                if node.right:
                    dfs(node.right,path)

        dfs(root,'')
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    leftright = TreeNode(5)
    left.right = leftright
    print(Solution().binaryTreePaths(root))