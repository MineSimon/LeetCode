"""
动态规划
计算公式: dp[j] += dp[j-1]
"""

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j-1]
        return dp[-1]

"""
可看做组合问题
从m+n-2步中取m-1个向右，即C(m+n-2, m-1)
"""
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 1
        for i in range(1, n):
            res *= (m + n - 1 - i)
            res /= i
        # round 就近取整
        return round(res)


if __name__ == '__main__':
    s = Solution2()
    print(s.uniquePaths(2,100))
