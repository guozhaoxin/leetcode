#encoding:utf8
__author__ = 'gold'

'''
Implement Queue using Stacks

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dataStack = []
        self.haha = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.dataStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.dataStack:
            self.haha.append(self.dataStack.pop())
        temp = self.haha.pop()
        while self.haha:
            self.dataStack.append(self.haha.pop())
        return temp

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.dataStack:
            self.haha.append(self.dataStack.pop())
        temp = self.haha[-1]
        while self.haha:
            self.dataStack.append(self.haha.pop())
        return temp

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.dataStack) == 0
