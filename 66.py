# Runtime: 20 ms, faster than 100.00% of Python online submissions for Plus One.
# Difficulty: Easy

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i], carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
            if carry == 0:
                return digits
        if carry:
            return [1] + digits
        return digits
