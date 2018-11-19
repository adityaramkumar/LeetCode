# Runtime: 56 ms, faster than 55.21% of Python online submissions for Transpose Matrix.
# Difficulty: Easy

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """        
        transpose = list()
        for i in range(len(A[0])):
            row = list()
            for j in range(len(A)):
                row.append(A[j][i])
            transpose.append(row)
        return transpose
