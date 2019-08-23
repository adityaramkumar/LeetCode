# Runtime: 96 ms, faster than 90.53% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 14.5 MB, less than 5.55% of Python3 online submissions for Minimum Window Substring.
# Difficulty: Hard

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chars = dict()
        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1
        
        start, end = 0, 0
        dist_chars = len(t_chars)
        final_string, min_len = "", float('inf')
        
        while end < len(s):
            if s[end] in t:
                t_chars[s[end]] -= 1
                if t_chars[s[end]] == 0:
                    dist_chars -= 1
            end += 1
            
            while dist_chars == 0:
                if end - start < min_len:
                    final_string = s[start:end]
                    min_len = end - start
            
                if s[start] in t_chars:
                    t_chars[s[start]] += 1
                    if t_chars[s[start]] == 1:
                        dist_chars += 1

                start += 1
                
        return final_string
                    
