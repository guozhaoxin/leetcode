#encoding:utf8
__author__ = 'gold'

'''
437.
Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''


from common.tree import TreeNode,midOrder


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.results = 0

        def dfs(node,leftSum):
            if not node:
                return
            if node.val == leftSum:
                self.results += 1

            dfs(node.left,)
            dfs(node.right,curSum + node.val)
            dfs(node.left,curSum)
            dfs(node.right,curSum)

        dfs(root,sum)
        return self.results


if __name__ == '__main__':
    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(-3)
    root.left = left
    root.right = right
    leftleft = TreeNode(3)
    leftright = TreeNode(2)
    left.left = leftleft
    left.right = leftright
    rightright = TreeNode(11)
    right.right = rightright
    leftleftleft = TreeNode(3)
    leftleftright = TreeNode(-2)
    leftleft.left = leftleftleft
    leftleft.right = leftleftright
    leftrightright = TreeNode(1)
    leftright.right = leftrightright
    # midOrder(root)
    print(Solution().pathSum(root,8))
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().pathSum(root,2))