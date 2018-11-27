# Runtime: 76 ms, faster than 56.93% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Difficulty: Easy

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter, length = 0, len(nums)
        while counter < length - 1:
            if nums[counter] == nums[counter + 1]:
                nums.pop(counter)
                length -= 1
            else:
                counter += 1
        return length
