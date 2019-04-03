"""
动态规划
计算公式: dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
"""

class Solution:
    def minPathSum(self, grid: list) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        # 初始化第一层
        for i in range(1,n):
            dp[i] = dp[i-1] + grid[0][i]
        # 从第二层开始计算
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

