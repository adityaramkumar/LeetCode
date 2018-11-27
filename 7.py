# Runtime: 52 ms, faster than 99.24% of Python3 online submissions for Reverse Integer.
# Difficulty: Easy

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative, reversed_x = x < 0, 0
        x = abs(x)
        
        while x:
            x, reversed_x = x // 10, reversed_x * 10 + x % 10
        if -2 ** 31 <= reversed_x <= 2 ** 31:
            return -reversed_x if negative else reversed_x
        return 0
