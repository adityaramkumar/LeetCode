# Runtime: 36 ms, faster than 99.72% of Python3 online submissions for Longest Common Prefix.
# Difficulty: Easy

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rstring = ''
        if not strs:
            return ''
        for i in range(min([len(string) for string in strs])):
            if all([string[i] == strs[0][i] for string in strs]):
                rstring += strs[0][i]
            else:
                return rstring
        return rstring
