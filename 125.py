# Runtime: 80 ms, faster than 42.27% of Python3 online submissions for Valid Palindrome.
# Difficulty: Easy

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.clean_string(s)
        return s == s[::-1]
        
    def clean_string(self, s):
        return ''.join([char.lower() for char in s if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122])
