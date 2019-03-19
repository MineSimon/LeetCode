class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        m1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        m2={"V":4,"X":9}
        m3={"L":40,"C":90}
        m4={"D":400,"M":900}
        i = 0
        while i < len(s):
            if s[i] == "I" or s[i] == "X" or s[i] == "C":
                if i+1 < len(s):
                    if s[i] == "I":
                        if s[i+1] == "V" or s[i+1] == "X":
                            ans += m2[s[i+1]]
                            i += 1
                        else:
                            ans += m1[s[i]]
                    elif s[i] == "X":
                        if s[i+1] == "L" or s[i+1] == "C":
                            ans += m3[s[i+1]]
                            i += 1
                        else:
                            ans += m1[s[i]]
                    else:
                        if s[i+1] == "D" or s[i+1] == "M":
                            ans += m4[s[i+1]]
                            i += 1
                        else:
                            ans += m1[s[i]]
                else:
                    ans += m1[s[i]]
            else:
                ans += m1[s[i]]
            i+= 1
        return ans


# 我对规则好像还不是很理解，应该是排序有一定的规则，比如：I不可能出现在M 的左边
class Solution2:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        if s == "":
            return 0

        index = len(s) - 2
        sum = ROMAN[s[-1]]
        while index >= 0:
            if ROMAN[s[index]] < ROMAN[s[index + 1]]:
                sum -= ROMAN[s[index]]
            else:
                sum += ROMAN[s[index]]
            index -= 1
        return sum


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("IX"))