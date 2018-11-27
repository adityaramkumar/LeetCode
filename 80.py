# Runtime: 52 ms, faster than 89.12% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# Difficulty: Medium

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter, length = 0, len(nums)
        while counter < length - 2:
            if nums[counter] == nums[counter + 2]:
                nums.pop(counter)
                length -= 1
            else:
                counter += 1
        return length
