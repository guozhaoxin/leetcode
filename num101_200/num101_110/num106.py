#encoding:utf8
__author__ = 'gold'

'''
Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        assert len(inorder) == len(postorder)
        if len(inorder) == 0:
            return

        def dfs(inLeft,inRight,postLeft,postRight):
            if postRight < 0 or inRight < 0 or postLeft < 0 or postRight < 0 :
                return
            if inLeft > inRight:
                return

            if inLeft == inRight:
                return TreeNode(postorder[postRight])

            node = TreeNode(postorder[postRight]) #得到根节点
            index = 0
            while inorder[index] != postorder[postRight]:
                index += 1

            #index得到的是中序遍历中根节点所在位置
            node.left = dfs(inLeft,index - 1,postLeft,postLeft + index - inLeft - 1)
            node.right = dfs(index + 1,inRight,postLeft + index - inLeft,postRight - 1)
            return node

        return dfs(0,len(inorder) - 1,0,len(postorder) - 1)


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def build(mark):
            if inorder and inorder[-1] != mark:
                root = TreeNode(postorder.pop())
                root.right = build(root.val)
                inorder.pop()
                root.left = build(mark)
                return root
            return None

        return build(None)

if __name__ == '__main__':
    # preorder = [3, 9, 20, 15, 7]
    preorder = [3,2,1,4]
    # inorder = [9, 3, 15, 20, 7]
    inorder = [1,2,3,4]
    root = Solution().buildTree(preorder,inorder)
    from common.tree import midOrder
    midOrder(root)