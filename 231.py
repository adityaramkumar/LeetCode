# Runtime: 56 ms, faster than 84.58% of Python3 online submissions for Power of Two.
# Difficulty: Easy

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 1:
            return n == 1
        return self.isPowerOfTwo(n/2)
