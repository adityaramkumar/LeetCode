# Runtime: 92 ms, faster than 22.41% of Python3 online submissions for Minimum Path Sum.
# Difficulty: Medium

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def memoize(fn):
            cache = dict()
            def memoized_fn(grid, row, col):
                if (row, col) in cache:
                    return cache[(row, col)]
                cache[(row, col)] = fn(grid, row, col)
                return cache[(row, col)]
            return memoized_fn
        
        @memoize
        def helper(grid, row, col):
            if row >= len(grid) or col >= len(grid[row]):
                return float('inf')
            if row == len(grid) - 1 and col == len(grid[row]) - 1:
                return grid[row][col]
            return grid[row][col] + min(helper(grid, row + 1, col), 
                       helper(grid, row, col + 1))
        return helper(grid, 0, 0)
