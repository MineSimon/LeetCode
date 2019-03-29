class Solution:
    def countAndSay(self, n: int) -> str:
        x = '1'
        res = ''
        while n != 1:
            l = len(x)
            count = 0
            temp = 0
            for i in range(l):
                if count == 0:
                    temp = x[i]
                    count += 1
                elif temp == x[i]:
                    count += 1
                elif temp != x[i]:
                    res += str(count)
                    res += temp
                    count = 1
                    temp = x[i]
            if count != 0:
                res += str(count)
                res += temp
            x = res
            res = ''
            n -= 1
        return x


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(10))
