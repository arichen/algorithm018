class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        loc, di = [0, 0], 0
        s = set(map(tuple, obstacles))
        res = 0

        for c in commands:
            if c == -2:
                di = (di - 1 + 4) % 4
            if c == -1:
                di = (di + 1) % 4
            else:
                for i in range(c):
                    if (loc[0] + dirs[di][0], loc[1] + dirs[di][1]) in s:
                        break
                    else:
                        loc[0] = loc[0] + dirs[di][0]
                        loc[1] = loc[1] + dirs[di][1]
                        res = max(res, loc[0] * loc[0] + loc[1] * loc[1])
        return res