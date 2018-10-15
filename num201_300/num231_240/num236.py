#encoding:utf8
__author__ = 'gold'

'''
Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        if not root:
            return None
        if p == q:
            return p

        def dfs(node,one,two):
            # if node:
            #     print(node.val)
            # else:
            #     print(node)
            if not node:
                return None,one,two

            if not one and not two:
                #两个节点都不存在
                if node.val == p.val:
                    result = dfs(node.left,node,two)
                    if result[2]:
                        return node,node,result[2]
                    result = dfs(node.right,node,two)
                    if result[2]:
                        return node,node,result[2]
                    return None,node,two

                if node.val == q.val:
                    result = dfs(node.left,one,node)
                    if result[1]:
                        return node,result[1],node
                    result = dfs(node.right,one,node)
                    if result[1]:
                        return node,result[1],node
                    return None,one,node

                result = dfs(node.left,one,two)
                if result[0]:
                    return result
                result = dfs(node.right,result[1],result[2])
                if result[0]:
                    return result
                if result[1] and result[2]:
                    return node,result[1],result[2]
                return None,result[1],result[2]

            if one:
                if node.val == q.val:
                    return None,one,node
                result = dfs(node.left,one,two)
                if result[2]:
                    return None,one,result[2]
                result = dfs(node.right,one,two)
                if result[2]:
                    return None,one,result[2]
                return None,one,two

            if two:
                if node.val == p.val:
                    return None,node,two
                result = dfs(node.left,one,two)
                if result[1]:
                    return None,result[1],two
                result = dfs(node.right,one,two)
                if result[1]:
                    return None,result[1],two
                return None,one,two

        result = dfs(root,None,None)
        if not result[0]:
            return root
        return result[0]


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        dp = {}

        def search(node, p):
            if not node:
                return False
            if (node, p) in dp:
                return dp[(node, p)]
            if node == p or search(node.left, p) or search(node.right, p):
                dp[(node, p)] = True
                return True
            else:
                dp[(node, p)] = False
                return False

        def binary(node, p, q):
            pLeft = search(node.left, p)
            qLeft = search(node.left, q)
            if node in {p, q}:
                return node

            if pLeft and qLeft:
                return binary(node.left, p, q)
            elif not pLeft and not qLeft:
                return binary(node.right, p, q)
            else:
                return node

        if search(p, q):
            return p
        if search(q, p):
            return q

        return binary(root, p, q)


if __name__ == '__main__':
    # root = TreeNode(3)
    # left = TreeNode(5)
    # right = TreeNode(1)
    # root.left = left
    # root.right = right
    # leftleft = TreeNode(6)
    # leftright = TreeNode(2)
    # left.left = leftleft
    # left.right = leftright
    # leftrightleft = TreeNode(7)
    # lefttrightright = TreeNode(4)
    # leftright.left = leftrightleft
    # leftright.right = lefttrightright
    # rightleft = TreeNode(0)
    # rightright = TreeNode(8)
    # right.left = rightleft
    # right.right = rightright
    #
    # print(Solution().lowestCommonAncestor(root,leftrightleft,right).val)

    root = TreeNode(9)
    left = TreeNode(-1)
    right = TreeNode(-4)
    root.left = left
    root.right = right
    leftleft = TreeNode(10)
    leftright = TreeNode(3)
    left.left = leftleft
    left.right = leftright
    leftleftright = TreeNode(5)
    leftleft.right = leftleftright
    print(Solution().lowestCommonAncestor(root,leftright,leftleftright).val)