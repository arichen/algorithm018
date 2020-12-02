# Idea:
# Find the minimum diff of two strings
#
# Subproblem:
# min diff of word1[1..i] and word2[1..j] can be determined by
# f(w1[1..(i-1)], w2[1..j]), f(w1[1..i], w2[1..(j-1)]), f(w1[1..(i-1)], w2[1..(j-1)])
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base case:
        # first row and col is diff between empty string and word1 or word2
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[-1][-1]