class Solution:
    res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        def _recur(l, path):
            if not l:
                self.res.append(path)
                return
            for i in range(len(l)):
                _recur(l[:i] + l[i + 1:], path + [l[i]])

        self.res = []
        _recur(nums, [])
        return self.res