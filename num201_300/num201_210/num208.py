#encoding:utf8
__author__ = 'gold'

'''
208.
Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        if not self.root:
            self.root = Node(word)
        else:
            if self.root.value == word:
                return
            elif self.root.value < word:
                self.root.right = self.__inseretHelp(self.root.right,word)
            else:
                self.root.left = self.__inseretHelp(self.root.left,word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        while node:
            if node.value == word:
                return True
            elif node.value < word:
                node = node.right
            else:
                node = node.left

        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        while node:
            if node.value.startswith(prefix):
                return True
            lengthen = min(len(prefix),len(node.value))
            if node.value[:lengthen] == prefix[:lengthen]:
                node = node.right
            elif node.value[:lengthen] > prefix[:lengthen]:
                node = node.left
            else:
                node = node.right

        return False

    def __inseretHelp(self,node,word):
        if node is None:
            return Node(word)
        if node.value == word:
            return node
        if node.value < word:
            node.right = self.__inseretHelp(node.right,word)
            return node
        else:
            node.left = self.__inseretHelp(node.left,word)
            return node

    def midOrder(self):
        results = []
        def dfs(node):
            if node:
                dfs(node.left)
                results.append(node.value)
                dfs(node.right)
        dfs(self.root)
        print(results)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    obj = Trie()
    obj.insert('p')
    obj.insert('pr')
    obj.insert('pre')
    print(obj.search('pre'))
    print(obj.startsWith('pre'))
    obj.midOrder()