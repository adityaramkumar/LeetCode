# Runtime: 40 ms, faster than 75.14% of Python3 online submissions for Unique Paths II.
# Difficulty: Medium

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp_grid = [[0 for i in range(len(obstacleGrid[0]))] 
                   for j in range(len(obstacleGrid))]
        dp_grid[len(dp_grid)-1][len(dp_grid[0])-1] = 1
        
        for row in range(len(obstacleGrid)-1, -1, -1):
            for col in range(len(obstacleGrid[row])-1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dp_grid[row][col] = 0
                    continue
                if row + 1 < len(obstacleGrid):
                    dp_grid[row][col] += dp_grid[row+1][col]
                if col + 1 < len(obstacleGrid[row]):
                    dp_grid[row][col] += dp_grid[row][col+1]
        return dp_grid[0][0]
