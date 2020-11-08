class Solution:
    res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        def _backtrack(level, start, path):
            if level == k:
                self.res.append(path)
                return

            for i in range(start, n + 1):
                _backtrack(level + 1, i + 1, path + [i])

        self.res = []
        _backtrack(0, 1, [])
        return self.res