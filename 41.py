# Runtime: 40 ms, faster than 77.30% of Python3 online submissions for First Missing Positive.
# Difficulty: Hard

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        for num in nums:
            visited.add(num)
        
        for i in range(1, len(nums) + 2):
            if i not in visited:
                return i
