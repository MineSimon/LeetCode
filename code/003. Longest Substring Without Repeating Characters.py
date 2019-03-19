class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        通过判断字符是否在子串中:
        如果遇到相同的字符, 就停止添加子串,
        记录当前最大的子串长度, 并使指针i返回到重复字符的后一个继续判断
        循环结束不能忘记判断最后子串的长度是否符合要求
        """
        max = 0
        i = 0
        curmax = 0
        substr = ""  # 当前的子串
        length = len(s)

        while i < length:
            # find 返回距离字符串最近的一个值
            # 若不存在相同字符, 就返回 -1
            index = substr.find(s[i])  # 注意使用[]
            if index == -1:
                substr += s[i]
                curmax += 1
            else:
                if max < curmax:
                    max = curmax
                curmax = 0
                substr = ""
                i = i - len(substr) + index  # 指针回溯
            i += 1

        if max < curmax:
            max = curmax

        return max


if __name__ == '__main__':
    s = Solution()
    str_ = "asdfwefsdcdvdadasfsd"
    max = s.lengthOfLongestSubstring(str_)
    print(max)
