# Idea:
# If m[i][j] is 1, it can form square of smallest common sqaure length with m[i-1][j-1], m[i-1][j], m[i][j-1].
#
# Subproblem:
# if m[i][j] == 1:
#   f(i, j) = min(f(i-1, j-1), f(i-1, j), f(i, j-1)) + 1
# else:
#   f(i, j) = 0
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # add additional row and col to run through first row and col

        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_len = max(dp[i][j], max_len)
        return max_len * max_len