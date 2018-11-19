# Runtime: 48 ms, faster than 93.38% of Python online submissions for Min Stack.
# Difficulty: Easy

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x == self.min:
            self.min = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
