# Runtime: 40 ms, faster than 98.68% of Python3 online submissions for Intersection of Two Arrays II.
# Difficulty: Easy

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1, intersection = dict(), list()
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
        for num in nums2:
            if dict1.get(num, 0) > 0:
                intersection.append(num)
                dict1[num] -= 1
        return intersection
