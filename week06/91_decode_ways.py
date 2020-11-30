# Idea:
# For each code, it can either be considered as single digit by itself, or double digit with previous code.
# If it can be considered single digit, use the number of ways up to previous code.
# If it can be considered as double digit, use the number of ways up to two letters before.
#
# Subproblem (roughly): f(n) = f(n-1) + f(n-2)
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        a0, a1 = 1, 1 if int(s[0] != "0") else 0
        for i in range(1, len(s)):
            temp = a1 if s[i] != "0" else 0

            n = int(s[i - 1: i + 1])
            if n >= 10 and n <= 26:
                temp += a0

            a0, a1 = a1, temp
        return a1