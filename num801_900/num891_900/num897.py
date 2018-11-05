#encoding:utf8
__author__ = 'gold'

'''
897.
Increasing Order Search Tree

Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
'''

from common.tree import TreeNode,midOrder


class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        temp = TreeNode('0')
        previous = temp
        queue = []
        cur = root
        preright = None

        while cur or queue:
            pass

        return temp.right

# class Solution:
#     def increasingBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         if not root:return
#
#         queue = []
#         vals = []
#         cur = root
#
#         while cur or queue:
#             while cur:
#                 queue.append(cur)
#                 cur = cur.left
#             if queue:
#                 vals.append(queue[-1].val)
#                 cur = queue.pop().right
#         root = TreeNode(vals[0])
#         temp = root
#         for i in range(1,len(vals)):
#             cur = TreeNode(vals[i])
#             temp.right = cur
#             temp = cur
#         return root

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        def helper(root):
            if not root:
                return
            left = helper(root.left)
            right = helper(root.right)
            if left:
                first = left[0]
                left[1].right = root
                root.left = None
            else:
                first = root
            if right:
                last = right[1]
                root.right = right[0]
            else:
                last = root
            return [first,last]
        return helper(root)[0]


if __name__ == '__main__':
    root = TreeNode(5)
    left = TreeNode(3)
    right = TreeNode(6)
    root.left = left
    root.right = right
    leftleft = TreeNode(2)
    leftright = TreeNode(4)
    left.left = leftleft
    left.right = leftright
    leftleftleft = TreeNode(1)
    leftleft.left = leftleftleft
    rightright = TreeNode(8)
    right.right = rightright
    rightrightleft = TreeNode(7)
    rightrightright = TreeNode(9)
    rightright.left = rightrightleft
    rightright.right = rightrightright
    midOrder(root)
    root = Solution().increasingBST(root)
    midOrder(root)