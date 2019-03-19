"""
20. 有效的括号(Valid Parentheses)
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        用栈来操作，按顺序依次入栈
        当正要入栈的是括号的右边部分时，判断入栈的最右边是否与之匹配
        """
        pars = []
        parmap = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in parmap:
                if pars == []:
                    return False
                elif parmap[i] != pars.pop():
                    return False
            else:
                pars.append(i)
        return pars == []


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('[([)]'))
