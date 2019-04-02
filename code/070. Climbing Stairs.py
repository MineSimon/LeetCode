# 动态规划
# 状态转移方程为
# dp[i] = dp[i-1] + dp[i-2]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1 for _ in range(n)]
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
