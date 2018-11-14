# Runtime: 20 ms, faster than 97.12% of Python online submissions for Word Pattern.
# Difficulty: Easy

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        if (len(pattern) != len(words)):
            return False
        
        matches = dict()
        for i in range(len(pattern)):
            if pattern[i] in matches and matches[pattern[i]] != words[i]:
                return False
            else:
                matches[pattern[i]] = words[i]
                
        vals = set()
        for element in matches.values():
            if element in vals:
                return False
            vals.add(element)
            
        return True
