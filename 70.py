# Runtime: 20 ms, faster than 96.64% of Python online submissions for Climbing Stairs.
# Difficulty: Easy

class Solution(object):
    def memoize(fn):
        cache = dict()
        def memoized_fn(self, n):
            if n in cache:
                return cache[n]
            cache[n] = fn(self, n)
            return cache[n]
        return memoized_fn
            
    @memoize
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
