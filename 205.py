# Runtime: 36 ms, faster than 58.66% of Python online submissions for Isomorphic Strings.
# Difficulty: Easy

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        hashmap = dict()
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]] != t[i]:
                return False
            elif s[i] not in hashmap and t[i] in hashmap.values():
                return False
            hashmap[s[i]] = t[i]
        return True
