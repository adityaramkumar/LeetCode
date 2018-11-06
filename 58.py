# Runtime: 20 ms, faster than 99.23% of Python online submissions for Length of Last Word.
# Difficulty: Easy

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1]) if len(s.split()) > 0 else 0
