# Runtime: 36 ms, faster than 98.90% of Python3 online submissions for Valid Parentheses.
# Difficulty: Easy

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opens = {'(':0, '{':1, '[':2}
        closes = {')':0, '}':1, ']':2}
        stack = list()
        
        for char in s:
            if char in opens:
                stack.append(opens[char])
            elif char in closes and not stack or closes[char] != stack.pop():
                return False
        return len(stack) == 0
