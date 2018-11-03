#encoding:utf8
__author__ = 'gold'

'''
652.
Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
'''

from common.tree import TreeNode

class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        results = []
        if not root:
            return results
        visitedNodeDict = {}
        def dfs(node):
            if not node:
                return ''
            curStr = str(node.val) +'l' + dfs(node.left) + 'r' + dfs(node.right)
            if curStr not in visitedNodeDict:
                visitedNodeDict[curStr] = 1
            else:
                if visitedNodeDict[curStr] == 1:
                    visitedNodeDict[curStr] = 2
                    results.append(node)
            return curStr

        dfs(root)
        return results

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    leftleft = TreeNode(4)
    rightleft = TreeNode(2)
    rightright = TreeNode(4)
    left.left = leftleft
    right.left = rightleft
    right.right = rightright
    rightleftleft = TreeNode(4)
    rightleft.left = rightleftleft
    result = Solution().findDuplicateSubtrees(root)
    print(len(result))
    for node in result:
        print(node.val)

    print('************')
    root = TreeNode(0)
    left = TreeNode(0)
    root.left = left
    leftleft = TreeNode(0)
    left.left = leftleft
    right = TreeNode(0)
    root.right = right
    rightright = TreeNode(0)
    right.right = rightright
    rightrightright = TreeNode(0)
    rightright.right = rightrightright
    result = Solution().findDuplicateSubtrees(root)
    print(len(result))
    for node in result:
        print(node.val)