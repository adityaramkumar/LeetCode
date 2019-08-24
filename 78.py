# Runtime: 36 ms, faster than 92.40% of Python3 online submissions for Subsets.
# Memory Usage: 13.8 MB, less than 5.95% of Python3 online submissions for Subsets.
# Difficulty: Medium

class Solution:
    def backtrack(self, nums, k):
        self.powerset.append(list(self.subset))
        for i in range(k, len(nums)):
            self.subset.append(nums[i])
            self.backtrack(nums, i + 1)
            self.subset.pop()
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.powerset, self.subset = list(), list()
        self.backtrack(nums, 0)
        return self.powerset
