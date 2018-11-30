# Runtime: 44 ms, faster than 22.76% of Python3 online submissions for Implement Queue using Stacks.
# Difficulty: Easy

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1, self.stack2 = list(), list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

