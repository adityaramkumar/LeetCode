# Runtime: 36 ms, faster than 99.51% of Python3 online submissions for Rotate Image.
# Difficulty: Medium

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        
        #transpose
        for row in range(length):
            for col in range(row + 1, length):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                
        #flip horizontal
        for row in range(length // 2):
            for col in range(length):
                matrix[col][row], matrix[col][length-1-row] = matrix[col][length-1-row], matrix[col][row]
