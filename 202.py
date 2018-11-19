# Runtime: 24 ms, faster than 97.63% of Python online submissions for Happy Number.
# Difficulty: Easy

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = self.make_new_num(n)
        return True
    
    def make_new_num(self, n):
        total = 0
        while n:
            n, total = n // 10, total + (n % 10) ** 2
        return total
