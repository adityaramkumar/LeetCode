# Runtime: 168 ms, faster than 59.75% of Python online submissions for Sum of Square Numbers.
# Difficulty: Easy

from math import sqrt

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        pointer_l, pointer_r = 0, round(sqrt(c))
        while pointer_l <= pointer_r:
            sum_squares = pointer_l * pointer_l + pointer_r * pointer_r
            if sum_squares == c:
                return True
            if sum_squares > c:
                pointer_r -= 1
            if sum_squares < c:
                pointer_l += 1
        return False
