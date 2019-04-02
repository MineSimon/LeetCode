class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) < 2 and s != '0':
            return 1
        if s[0] == '0':
            return 0

        dp = [1, 1]
        for i in range(2, len(s) + 1):
            # print dp, s[i-2:i]
            # 当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，那么可以有两种编码方式（BA，U），所以dp[i]=dp[i-1]+dp[i-2]
            if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':
                dp.append(dp[i - 1] + dp[i - 2])
            # 当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，所以dp[i]=dp[i-2]
            elif int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:
                dp.append(dp[i - 2])
            # 当s[i-2:i]不在以上两个范围时，如09这种，编码方式为0，而31这种，dp[i]=dp[i-1]
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('101'))
