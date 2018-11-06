# Runtime: 40 ms, faster than 98.77% of Python3 online submissions for Subsets.
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
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        subsets = list()
        subsets.extend(self.subsets(nums[1:]))
        subsets.extend(map(lambda subset: [nums[0]] + subset, self.subsets(nums[1:])))
        return subsets
        
