class Solution:
    def hasGroupsSizeX(self, deck:list) -> bool:
        l = len(deck)
        if l < 2:
            return False
        s = sorted(deck)
        mod = 2
        m = l//2 + 2
        for mod in range(2,m):
            if l%mod == 0:
                i = 0
                while i<l:
                    j = 1
                    while j<mod:
                        if s[i] != s[i+j]:
                            break
                        j += 1
                    i += mod
                return True


# a>b
def gcd(a:int, b:int) -> int:
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)


if __name__ == "__main__":
    s = Solution()
    # print(s.hasGroupsSizeX([0,0,0,0,0,1,1,1,1,1]))
    print(gcd(10, 3))
