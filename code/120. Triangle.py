# 从上到下计算
class Solution1:
    def minimumTotal(self, triangle: list) -> int:
        for i in range(1,len(triangle)):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j]
                elif j < i:
                    triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
                else:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
        return triangle

# 从下到上计算
class Solution2:
    def minimumTotal(self, triangle: list) -> int:
        dp = triangle[-1]
        for i in range(len(dp)-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]


if __name__ == '__main__':
    s = Solution2()
    print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
