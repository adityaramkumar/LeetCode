# Runtime: 56 ms, faster than 97.01% of Python3 online submissions for Reverse Vowels of a String.
# Memory Usage: 14.3 MB, less than 36.60% of Python3 online submissions for Reverse Vowels of a String.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        pointer_left, pointer_right = 0, len(s) - 1
        s = list(s)
        
        while pointer_right > pointer_left:
            left_vowel, right_vowel = s[pointer_left] in vowels, s[pointer_right] in vowels
            if left_vowel and right_vowel:
                s[pointer_left], s[pointer_right] = s[pointer_right], s[pointer_left]
                pointer_left += 1
                pointer_right -= 1
            elif left_vowel:
                pointer_right -= 1
            elif right_vowel:
                pointer_left += 1
            else:
                pointer_left += 1
                pointer_right -= 1
        
        return ''.join(s)
    
    """Less elegant solution
    def reverseVowels(self, s: str) -> str:
        indices = set()
        vowels, consonants = queue.LifoQueue(), queue.Queue()
        
        for i in range(len(s)):
            if s[i] in vowels_set:
                vowels.put(s[i])
                indices.add(i)
            else:
                consonants.put(s[i])
                
        reversed_string = list()
        for i in range(len(s)):
            if i in indices:
                reversed_string.append(vowels.get())
            else:
                reversed_string.append(consonants.get())
            
        return ''.join(reversed_string)
    """
