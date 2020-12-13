# n & (n - 1): flips the least significant 1-bit to 0
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n &= n - 1
        return count