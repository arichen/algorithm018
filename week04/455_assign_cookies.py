class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = sorted(g), sorted(s)
        lg, ls = len(g), len(s)
        count, i, j = 0, 0, 0
        while i < lg and j < ls:
            if g[i] > s[j]:
                j += 1
            else:
                count += 1
                i += 1
                j += 1
        return count