# n & (n - 1): flips the least significant 1-bit to 0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and (n & (n - 1) == 0)