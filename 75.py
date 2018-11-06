# Runtime: 36 ms, faster than 99.88% of Python3 online submissions for Sort Colors.
# Difficulty: Medium

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        colors = dict()
        for num in nums:
            colors[num] = colors.get(num, 0) + 1
        
        i = -1
        for i in range(colors.get(0, 0)):
            nums[i] = 0
        for i in range(i+1, i+1+colors.get(1, 0)):
            nums[i] = 1
        for i in range(i+1, i+1+colors.get(2, 0)):
            nums[i] = 2
