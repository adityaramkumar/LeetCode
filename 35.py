# Runtime: 48 ms, faster than 29.06% of Python3 online submissions for Search Insert Position.
# Difficulty: Easy

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.si_helper(nums, target, 0, len(nums))
        
    def si_helper(self, nums, target, start, end):
        if start == end:
            return start
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            return self.si_helper(nums, target, start + 1, end)
        elif nums[middle] > target:
            return self.si_helper(nums, target, start, end - 1)            
