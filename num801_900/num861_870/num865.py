#encoding:utf8
__author__ = 'gold'

'''
865.
Smallest Subtree with all the Deepest Nodes

Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

 

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:



We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
 

Note:

The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.
'''

from common.tree import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        def helper(node,depth):
            '''
            :param node: TreeNode
            :param depth: int
            :return:
            '''
            if not node:
                return None
            leftres = helper(node.left,depth + 1)
            rightres = helper(node.right,depth + 1)
            if not leftres and not rightres:
                return [depth + 1,node]
            if leftres and rightres:
                if leftres[0] == rightres[0]:
                    return [leftres[0],node]
                elif leftres[0] > rightres[0]:
                    return leftres
                else:
                    return rightres
            if leftres:
                return leftres
            if rightres:
                return rightres
        return helper(root,1)[1]

if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(5)
    right = TreeNode(1)
    root.left = left
    root.right = right
    leftleft = TreeNode(6)
    left.left = leftleft
    leftright = TreeNode(2)
    left.right = leftright
    leftrightleft = TreeNode(7)
    leftrightright = TreeNode(2)
    leftright.left = leftrightleft
    leftright.right = leftrightright
    print(Solution().subtreeWithAllDeepest(root).val)