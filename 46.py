# Runtime: 52 ms, faster than 86.29% of Python3 online submissions for Permutations.
# Difficulty: Medium 

class Solution:
    def memoize(fn):
        cache = dict()
        def memoized_fn(self, nums):
            if tuple(nums) in cache:
                return cache[tuple(nums)]
            cache[tuple(nums)] = fn(self, nums)
            return cache[tuple(nums)]
        return memoized_fn
    
    @memoize
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        permutations = list()
        for i in range(len(nums)):
            for per in self.permute(nums[:i] + nums[i+1:]):
                permutations.append([nums[i]] + per)
        return permutations
