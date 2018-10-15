#encoding:utf8
__author__ = 'gold'

'''
 Construct Binary Tree from Preorder and Inorder Traversal
 
 Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        #先把特殊情况给干掉
        assert len(preorder) == len(inorder)
        if len(preorder) == 0:
            return

        def dfs(preLeft,preRight,inLeft,inRight):
            if preLeft > preRight:
                return
            if preLeft == preRight:
                return TreeNode(preorder[preLeft])

            headVal = preorder[preLeft] #当前根节点
            root = TreeNode(headVal)
            index = inLeft
            while inorder[index] != headVal:
                index += 1

            leftL = index - inLeft
            rightL = inRight - index

            root.left = dfs(preLeft + 1,preLeft + leftL,inLeft,index - 1)
            root.right = dfs(preLeft + leftL + 1,preRight,index + 1,inRight)

            return root

        return dfs(0,len(preorder) - 1,0,len(inorder) - 1)

if __name__ == '__main__':
    # preorder = [3, 9, 20, 15, 7]
    preorder = [3,2,1,4]
    # inorder = [9, 3, 15, 20, 7]
    inorder = [1,2,3,4]
    root = Solution().buildTree(preorder,inorder)
    from common.tree import midOrder
    midOrder(root)