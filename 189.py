# Runtime: 136 ms, faster than 21.79% of Python3 online submissions for Rotate Array.
# Difficulty: Easy

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
