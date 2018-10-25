# Runtime: 20 ms, faster than 98.94% of Python online submissions for Unique Paths.
# Difficulty: Medium

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp_grid = [[0 for i in range(m)] 
                   for j in range(n)]
        dp_grid[len(dp_grid)-1][len(dp_grid[0])-1] = 1
        
        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                if row + 1 < n:
                    dp_grid[row][col] += dp_grid[row+1][col]
                if col + 1 < m:
                    dp_grid[row][col] += dp_grid[row][col+1]
        return dp_grid[0][0]
