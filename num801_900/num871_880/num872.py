#encoding:utf8
__author__ = 'gold'

'''
872.
Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''

from common.tree import TreeNode

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        q1 = [root1]
        q2 = [root2]
        while q1 and q2:
            v1 = self.helper(q1)
            v2 = self.helper(q2)
            if v1 != v2:
                return False

        return not q1 and not q2


    def helper(self,stack):
        '''

        :param stack:List
        :return:
        '''
        while True:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            if (not node.right) and (not node.left):
                return node.val

if __name__ == '__main__':
    root1 = TreeNode(2)
    root1.left = TreeNode(2)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    print(Solution().leafSimilar(root1,root2))