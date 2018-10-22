# Runtime: 40 ms, faster than 51.57% of Python3 online submissions for House Robber.
# Difficulty: Easy

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def memoize(fn):
            cache = dict()
            def new_fn(lst):
                if len(lst) in cache:
                    return cache[len(lst)]
                cache[len(lst)] = fn(lst)
                return cache[len(lst)] 
            return new_fn
        
        @memoize
        def helper(nums):
            if len(nums) == 0:
                return 0
            return max(nums[0] + helper(nums[2:]),
                   helper(nums[1:]))
        return helper(nums)
