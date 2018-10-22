# Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Range Sum Query - Immutable.
# Difficulty: Easy

class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j] - self.nums[i-1] if i > 0 else self.nums[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
