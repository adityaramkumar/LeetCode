# Runtime: 20 ms, faster than 100.00% of Python online submissions for Two Sum II - Input array is sorted.
# Difficulty: Easy

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pointer1, pointer2 = 0, len(numbers) - 1
        while pointer1 != pointer2:
            sum = numbers[pointer1] + numbers[pointer2]
            if sum == target:
                return [pointer1 + 1, pointer2 + 1]
            elif sum > target:
                pointer2 -= 1
            else:
                pointer1 += 1
