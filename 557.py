# Runtime: 28 ms, faster than 76.71% of Python online submissions for Reverse Words in a String III.
# Difficulty: Easy

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda word: word[::-1], s.split(' ')))
