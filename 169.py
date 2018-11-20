# Runtime: 40 ms, faster than 54.99% of Python online submissions for Majority Element.
# Difficulty: Easy

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        values = dict()
        for num in nums:
            values[num] = values.get(num, 0) + 1
        return max(values, key=values.get)
