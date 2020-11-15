class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0}
        for b in bills:
            if b == 5:
                d[5] += 1
            elif b == 10:
                d[5], d[10] = d[5] - 1, d[10] + 1
            elif d[10] > 0:
                d[5], d[10] = d[5] - 1, d[10] - 1
            else:
                d[5] -= 3
            if d[5] < 0:
                return False
        return True