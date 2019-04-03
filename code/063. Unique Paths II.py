class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # 初始化第一层
        dp = [0 for _ in range(n)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[i] = 1

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j == 0:
                    pass
                elif dp[j] != 0 and dp[j - 1] != 0:
                    dp[j] += dp[j - 1]
                elif dp[j] == 0 and dp[j - 1] != 0:
                    dp[j] = dp[j - 1]
                elif dp[j] != 0 and dp[j - 1] == 0:
                    pass
                elif dp[j] == 0 and dp[j - 1] == 0:
                    pass
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,0]]))
