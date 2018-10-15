#encoding:utf8
__author__ = 'gold'

'''
Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = [root]
        count = 1
        while stack:
            child = []
            for node in stack:
                if node.left:
                    child.append(node.left)
                else:
                    return count + len(child)
                if node.right:
                    child.append(node.right)
                else:
                    return count + len(child)
            count += len(child)
            stack = child

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
          return 0
        cur = root
        count = 0 #高度
        while cur != None:
          count+=1
          cur = cur.left
        cur_root = root
        tmp_count = count
        l,r = 0, pow(2,count-1)
        while tmp_count >= 0:
          cur = cur_root.right
          if cur == None:
            break;
          sub_count = 1
          while cur != None:
            sub_count += 1
            cur = cur.left
          if sub_count == tmp_count:
            l = l + (r-l+1)//2
            cur_root = cur_root.right
          else:
            r = l + (r-l+1)//2
            cur_root = cur_root.left
          tmp_count -= 1
        return pow(2,count-1) + l


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    leftleft = TreeNode(4)
    leftright = TreeNode(5)
    left.left = leftleft
    left.right = leftright
    rightleft= TreeNode(6)
    right.left = rightleft
    print(Solution().countNodes(root))