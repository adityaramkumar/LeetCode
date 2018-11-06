# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Nim Game.
# Difficulty: Easy

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)
