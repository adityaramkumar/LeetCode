# Runtime: 776 ms, faster than 10.35% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Difficulty: Medium

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_max = 0
        for index in range(len(s)):
            visited, runner = set(), index
            while runner < len(s):
                if s[runner] in visited:
                    break
                visited.add(s[runner])
                runner += 1
            if len(visited) > len_max:
                len_max = len(visited)
        return len_max
