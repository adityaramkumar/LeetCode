# Runtime: 68 ms, faster than 22.13% of Python3 online submissions for Permutations.
# Difficulty: Medium 

class Solution:
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
