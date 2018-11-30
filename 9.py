# Runtime: 252 ms, faster than 98.38% of Python3 online submissions for Palindrome Number.
# Difficulty: Easy

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
