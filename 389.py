# Runtime: 40 ms, faster than 88.16% of Python3 online submissions for Find the Difference.
# Difficulty: Easy

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = dict()
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
            
        for letter in t:
            if letter not in letters or letters[letter] == 0:
                return letter
            letters[letter] -= 1
