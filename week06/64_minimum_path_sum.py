# Idea:
# Each grid can only be reached from top or left grid.
# The minimum path to a grid must come from either top or left grid.
#
# Subproblem (roughly): f(i, j) = min(f(top grid), f(left grid)) + grid(i, j)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]