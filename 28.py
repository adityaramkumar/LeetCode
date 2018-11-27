# Runtime: 36 ms, faster than 96.20% of Python3 online submissions for Implement strStr().
# Difficulty: Easy

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Use Rabin-Karp Algorithm
        if needle == haystack:
            return 0
        n_length, n_hash = len(needle), hash(needle)
        for i in range(len(haystack) - n_length + 1):
            if hash(haystack[i:i+n_length]) == n_hash and haystack[i:i+n_length] == needle:
                return i
        return -1
