# Runtime: 40 ms, faster than 69.04% of Python3 online submissions for Remove Element.
# Difficulty: Easy

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter, length = 0, len(nums)
        while counter < length:
            if nums[counter] == val:
                nums.pop(counter)
                length -= 1
            else:
                counter += 1
        return length
