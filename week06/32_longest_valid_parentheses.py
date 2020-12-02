# Idea:
# Each valid parentheses is consisted of other valid parentheses or empty string.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        max_len = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                left = (i - 1) if not dp[i - 1] else (i - dp[i - 1] - 1)
                # find the index where we should look for left bracket,
                # which is the first position to the left that are not part of a closed parentheses.

                if left >= 0 and s[left] == "(":
                    # a left bracket found. close the parentheses.

                    dp[i] = 2 + dp[i - 1] + (dp[left - 1] if left > 0 else 0)
                    # current local max length of valid parentheses is extended from previous max.

                    max_len = max(dp[i], max_len)
                    # update global max length
        return max_len