class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        注意：
        环境只能存贮32位有效数字, 所以在res增加时就需要判断, 不可在最后结果前进行
        这样很容易导致结果已经超出环境最大储存大小而导出出错
        """
        res = 0
        jud = 1
        max = 2 ** 31
        # 将数字x转换为正数,更方便进行判断
        if x < 0:
            x = -x
            jud = -1
        while True:
            add = x % 10
            x = x // 10
            # 判断res是否超过环境最大允许值
            if jud == 1 and (res > max // 10 or (res == max // 10 and add > 7)):
                return 0
            if jud == -1 and (res > max // 10 or (res == max // 10 and add > 8)):
                return 0

            res = res * 10 + add
            # 判断循环是否结束
            if x == 0:
                break

        return res * jud


if __name__ == '__main__':
    s = Solution()
    res = s.reverse(123)
    print(res)
    res = s.reverse(-123)
    print(res)
    res = s.reverse(120)
    print(res)
