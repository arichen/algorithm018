# Idea:
# Each palindromic string is constitued by palindromic substring
#
# Subproblem:
# f(s(i,j)) = {
#   True, if s[i] == s[j] and f(s(i+1, j-1));
#   False, otherwise
# }
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # base case: length 1
        for i in range(n):
            dp[i][i] = True

        # base case: length 2
        for i in range(1, n):
            dp[i - 1][i] = (s[i - 1] == s[i])

        # general case
        for l in range(3, n + 1): # iterate through substring lengths
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

        return sum([sum(r) for r in dp])