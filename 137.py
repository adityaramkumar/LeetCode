# Runtime: 44 ms, faster than 61.77% of Python3 online submissions for Single Number II.
# Difficulty: Medium

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
