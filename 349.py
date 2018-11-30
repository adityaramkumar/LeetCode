# Runtime: 48 ms, faster than 46.44% of Python3 online submissions for Intersection of Two Arrays.
# Difficulty: Easy

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        intersection = set()
        for num in nums2:
            if num in set1:
                intersection.add(num)
        return list(intersection)
