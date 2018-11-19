# Runtime: 20 ms, faster than 99.54% of Python online submissions for Reverse Words in a String.
# Difficulty: Medium

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        cleaned_list = list()
        for element in s.split(' ')[::-1]:
            if element != '':
                cleaned_list.append(element)
        return ' '.join(cleaned_list)
