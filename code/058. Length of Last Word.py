class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >=0 and s[i] != ' ':
            i -= 1
            count += 1
        return count


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        # strip 移除字符串头尾指定的字符，默认为空格或换行符
        s = s.strip()
        # split 通过指定分隔符对字符串进行切片，返回分割后的列表
        lst = s.split(' ')
        return len(lst[-1])


if __name__ == '__main__':
    s = Solution1()
    print(s.lengthOfLastWord('     '))
