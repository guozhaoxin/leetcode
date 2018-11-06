#encoding:utf8
__author__ = 'gold'

'''
889.
Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
'''

from common.tree import TreeNode,midOrder,preOrder,postOrder

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        assert len(pre) == len(post)

        def helper(preIndex,postSt,postEnd):
            if preIndex == len(pre):
                return None
            if postSt == postEnd:
                return TreeNode(post[postEnd])
            node = TreeNode(pre[preIndex])
            if preIndex == len(pre) - 1:
                return node
            childNum = pre[preIndex + 1]
            index = postSt
            while index < postEnd:
                if post[index] == childNum:
                    break
                index += 1
            if index == postEnd:
                print("wrong!")
            if index == postEnd - 1:
                node.right = None
                node.left = helper(preIndex + 1,postSt,postEnd - 1)
            else:
                node.left = helper(preIndex + 1,postSt,index)
                node.right = helper(preIndex + 2 + index - postSt,index + 1,postEnd - 1)

            return node
        return helper(0,0,len(post) - 1)

if __name__ == '__main__':
    pre = [1, 2, 4, 5, 3, 6, 7]
    post = [4, 5, 2, 6, 7, 3, 1]
    root = Solution().constructFromPrePost(pre,post)
    midOrder(root)
    preOrder(root)
    postOrder(root)