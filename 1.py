# Runtime: 36 ms, faster than 99.74% of Python3 online submissions for Two Sum.
# Difficulty: Easy

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        stored_values = dict()
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in stored_values:
                return [stored_values[diff], index]
            stored_values[nums[index]] = index
