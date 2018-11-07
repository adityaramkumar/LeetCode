# Runtime: 48 ms, faster than 58.80% of Python3 online submissions for Single Number.
# Difficulty: Easy

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequencies = dict()
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        return min(nums, key=frequencies.get)
        
