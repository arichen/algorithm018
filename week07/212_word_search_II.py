class Solution:
    END_OF_WORD = "#"
    VISITED = "-"
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    def __init__(self):
        self.board = None
        self.trie = None
        self.rows = 0
        self.cols = 0
        self.result = set()

    def initTrie(self, words: List[str]):
        self.trie = {}
        for w in words:
            node = self.trie
            for c in w:
                node = node.setdefault(c, {})
            node[self.END_OF_WORD] = self.END_OF_WORD

    def dfs(self, r: int, c: int, prefix: str, node: dict):
        if not (0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] in node):
            return

        prefix += self.board[r][c]
        node = node[self.board[r][c]]
        if self.END_OF_WORD in node:
            self.result.add(prefix)

        tmp, self.board[r][c] = self.board[r][c], self.VISITED
        for i in range(4):
            self.dfs(r + self.dy[i], c + self.dx[i], prefix, node)
        self.board[r][c] = tmp

    def initBoard(self, board: List[List[str]]):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.initTrie(words)
        self.initBoard(board)

        self.result = set()
        for i in range(self.rows):
            for j in range(self.cols):
                self.dfs(i, j, "", self.trie)
        return self.result
