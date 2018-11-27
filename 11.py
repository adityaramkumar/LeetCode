# Runtime: 68 ms, faster than 79.81% of Python3 online submissions for Container With Most Water.
# Difficulty: Medium

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        pointer_l, pointer_r = 0, len(height) - 1
        
        while pointer_l != pointer_r:
            area = (pointer_r - pointer_l) * min(height[pointer_l], height[pointer_r])
            if area > max_area:
                max_area = area
            
            if height[pointer_l] < height[pointer_r]:
                pointer_l += 1
            else:
                pointer_r -= 1
                
        return max_area
        
