#encoding:utf8
__author__ = 'gold'

'''
450.
Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        curNode = root
        parent = None
        while curNode:
            if curNode.val == key:
                break
            if curNode.val < key:
                parent = curNode
                curNode = curNode.right
            else:
                parent = curNode
                curNode = curNode.left

        #先处理没有找到节点的情况
        if not curNode:
            return root

        #处理节点为叶子的情况
        if not curNode.left and not curNode.right:
            #处理叶子是根节点
            if not parent:
                return None
            if curNode is parent.left:
                parent.left = None
            else:
                parent.right = None
            return root

        #处理被删除节点只有左子树的情况
        if not curNode.right:
            #先处理删除节点是根节点
            if not parent:
                return curNode.left
            if curNode is parent.left:
                parent.left = curNode.left
            else:
                parent.right = curNode.left
            return root

        #处理被删除节点只有右子树的情况
        if not curNode.left:
            if not parent:
                return curNode.right
            if curNode is parent.left:
                parent.left = curNode.right
            else:
                parent.right = curNode.right
            return root

        #处理俩子树都存在
        minKeyNode = curNode.right
        minParent = curNode
        while minKeyNode.left:
            minParent = minKeyNode
            minKeyNode = minKeyNode.left

        #被删除节点的右节点没有左子树
        if minKeyNode is curNode.right:
            minKeyNode.left = curNode.left
            if not parent:
                return minKeyNode
            if curNode is parent.left:
                parent.left = minKeyNode
            else:
                parent.right = minKeyNode
            return root

        minParent.left = minKeyNode.right
        minKeyNode.left = curNode.left
        minKeyNode.right = curNode.right
        if not parent:
            return minKeyNode
        if curNode is parent.left:
            parent.left = minKeyNode
        else:
            parent.right = minKeyNode
        return root