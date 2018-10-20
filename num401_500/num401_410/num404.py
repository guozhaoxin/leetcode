#encoding:utf8
__author__ = 'gold'

'''
404.
Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''


from common.tree import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        def dfs(parent,node,result):
            if not node.left and not node.right:
                if node is parent.left:
                    result[0] += node.val
                    return
            if node.left:
                dfs(node,node.left,result)
            if node.right:
                dfs(node,node.right,result)

        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        if root.left:
            dfs(root,root.left,result)
        if root.right:
            dfs(root,root.right,result)
        return result[0]

if __name__ == '__main__':
    print(Solution().sumOfLeftLeaves(None))