# Runtime: 40 ms, faster than 99.52% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Difficulty: Medium

from operator import add, sub, mul

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        operators = {'+': add, '-': sub, '*': mul, 
                     '/': lambda x, y: x // y if x / y >= 0 else 
                     -(abs(x) // abs(y))}
        for token in tokens:
            if token in operators:
                val2, val1 = stack.pop(), stack.pop()
                stack.append(operators[token](val1, val2))
            else:
                stack.append(int(token))
        return stack[0]
    
