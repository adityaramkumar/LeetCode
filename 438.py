# Runtime: 136 ms, faster than 53.95% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 14.9 MB, less than 8.70% of Python3 online submissions for Find All Anagrams in a String.
# Difficulty: Medium

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return list()
        
        p_chars = dict()
        for char in p:
            p_chars[char] = p_chars.get(char, 0) + 1
        
        distinct = len(p_chars)
        output = list()
        
        for i in range(len(p)):
            if s[i] in p_chars:
                p_chars[s[i]] -= 1
                if p_chars[s[i]] == 0:
                    distinct -= 1
            if distinct == 0:
                output.append(0)
        
        index = 1
        while index + len(p) <= len(s):
            if s[index - 1] in p_chars:
                p_chars[s[index - 1]] += 1
                if p_chars[s[index - 1]] == 1:
                    distinct += 1
            
            if s[index + len(p) - 1] in p_chars:
                p_chars[s[index + len(p) - 1]] -= 1
                if p_chars[s[index + len(p) - 1]] == 0:
                    distinct -= 1
            if distinct == 0:
                output.append(index)
            
            index += 1
        
        return output
