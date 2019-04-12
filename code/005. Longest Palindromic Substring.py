class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        res = ''

        for i in range(1, len(s)):

            # 'bab'奇数情况
            temp = s[i]
            n = 1
            while i-n >= 0 and i+n < len(s):
                if s[i-n] == s[i+n]:
                    temp = s[i-n] + temp + s[i+n]
                    n += 1
                else:
                    break
            if len(temp) > len(res):
                res = temp

            # 'saas' 偶数情况
            if s[i] == s[i-1]:
                temp = s[i-1:i+1]
                n = 1
                while i-1-n >= 0 and i+n < len(s):
                    if s[i-1-n] == s[i+n]:
                        temp = s[i-1-n] + temp + s[i+n]
                        n += 1
                    else:
                        break
                if len(temp) > len(res):
                    res = temp

        return res


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        q = '#'+'#'.join(s)+'#'
        n = len(q)
        maxl = 1 #当前最长的回文串半径
        m = 0  #当前最长的回文串中心
        l = [1 for i in range(n)] #元素最长的回文串半径
        y = 0  #所在回文串的最右点
        z = 0  #所在回文串的中心点
        for i in range(1,n-1):
            if i < y:
                l[i] = min(l[2*z-i], y-i) #i的回文串至少拥有的半径
            try:
                while q[i+l[i]] == q[i-l[i]]:
                    l[i] += 1
            except: pass
            if l[i] > maxl:
                maxl = l[i]
                m = i
            if i+l[i] == n:
                break
            if i+l[i] > y:
                z = i
                y = i+l[i]

        return s[(m-maxl+1)//2:(m+maxl)//2]


if __name__ == "__main__":
    s = Solution2()
    print(s.longestPalindrome("baab"))
