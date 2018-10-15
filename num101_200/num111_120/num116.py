#encoding:utf8
__author__ = 'gold'

'''
Populating Next Right Pointers in Each Node

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
'''


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        stack = []
        stack.append(root)
        stack.append(None)

        index = 0
        while index < len(stack) and stack[index]:
            while index < len(stack) and stack[index]:
                stack.append(stack[index].left)
                stack.append(stack[index].right)
                index += 1
            stack.append(None)
            index += 1
        index = 0
        while index < len(stack):
            while index < len(stack) and stack[index]:
                stack[index].next = stack[index + 1]
                index += 1
            index += 1

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        curr = dummy = root
        while dummy and dummy.left:
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            curr = dummy.left
            dummy = dummy.left