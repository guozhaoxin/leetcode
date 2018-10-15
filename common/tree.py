#encoding:utf8
__author__ = 'gold'

def preOrder(root):
    results = []
    def dfs(node):
        if not node:
            return
        results.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    print(results)

def midOrder(root):
    results = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        results.append(node.val)
        dfs(node.right)
    dfs(root)
    print(results)

def postOrder(root):
    results = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        results.append(node.val)
    dfs(root)
    print(results)