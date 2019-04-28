class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self._gen(n, 0, 0, '')
        return self.ans

    def _gen(self, n, left, right, result):

        # 判断是否生成结束
        if left == n and right == n:
            self.ans.append(result)
            return
        # 判断是否左右括号相等，只能生成左括号
        elif left < n and left == right:
            self._gen(n, left + 1, right, result + '(')
        # 当左右括号不等，有两种情况
        elif left < n and left > right:
            self._gen(n, left + 1, right, result + '(')
            self._gen(n, left, right + 1, result + ')')
        # 左括号生成完成，只增加右括号
        else:
            self._gen(n, left, right + 1, result + ')')
