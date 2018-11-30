# Runtime: 112 ms, faster than 99.97% of Python3 online submissions for Group Anagrams.
# Difficulty: Medium

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = dict()
        for element in strs:
            key = ''.join(sorted(element))
            if key in anagrams:
                anagrams[key].append(element)
            else:
                anagrams[key] = [element]
        return list(anagrams.values())
