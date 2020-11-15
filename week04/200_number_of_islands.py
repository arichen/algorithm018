class Solution:
    def __init__(self):
        self.grid = None
        self.m = 0
        self.n = 0

    def dfsMarking(self, i: int, j: int):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.grid[i][j] == "0":
            return

        self.grid[i][j] = "0"
        self.dfsMarking(i, j + 1)
        self.dfsMarking(i, j - 1)
        self.dfsMarking(i + 1, j)
        self.dfsMarking(i - 1, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfsMarking(i, j)

        return count