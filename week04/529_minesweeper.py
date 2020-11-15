class Solution:
    def __init__(self):
        self.board = None
        self.m = None
        self.n = None
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def isOutOfBound(self, x: int, y: int) -> bool:
        return x < 0 or x >= self.m or y < 0 or y >= self.n

    def hasMine(self, x: int, y: int) -> bool:
        return not self.isOutOfBound(x, y) and self.board[x][y] == "M"

    def adjacentMine(self, x: int, y: int) -> int:
        count = 0
        for dx, dy in self.directions:
            count += self.hasMine(x + dx, y + dy)
        return count

    def revealBoard(self, x: int, y: int):
        if self.isOutOfBound(x, y) or not self.board[x][y] in ("M", "E"):
            return

        # mine, reveal and return
        if self.board[x][y] == "M":
            self.board[x][y] = "X"
            return

        # has adjacent mines, mark number and return
        count = self.adjacentMine(x, y)
        if count:
            self.board[x][y] = str(count)
            return

        # blank field, mark and reveal adjacent grids
        self.board[x][y] = "B"
        for dx, dy in self.directions:
            self.revealBoard(x + dx, y + dy)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.board, self.m, self.n = board, len(board), len(board[0])
        self.revealBoard(*click)
        return self.board