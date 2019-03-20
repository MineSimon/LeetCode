# 解法1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 将a转换中a,b中的大数
        if len(a) < len(b):
            temp = a
            a = b
            b = temp
        l1 = len(a)
        l2 = len(b)
        i = 0
        j = 0
        res = ''
        while i < l1:
            if i < l2:
                temp = int(a[l1 - i - 1]) + int(b[l2 - i - 1]) + j
                # 判断进位
                if temp == 0 or temp == 1:
                    res = str(temp) + res
                    j = 0
                elif temp == 2:
                    res = '0' + res
                    j = 1
                else:
                    res = '1' + res
                    j = 1
                i += 1
            else:
                temp = int(a[l1 - i - 1]) + j
                # 判断进位
                if temp == 0 or temp == 1:
                    res = str(temp) + res
                    j = 0
                else:
                    res = '0' + res
                    j = 1
                i += 1
        if j == 1:
            res = '1' + res
        return res


# 解法2
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        # 将两个补齐长度
        if len(a) < len(b):
            while len(a) < len(b):
                a = '0' + a
        elif len(a) > len(b):
            while len(a) > len(b):
                b = '0' + b
        l = len(a) - 1
        j = 0
        res = ''
        while l >= 0:
            temp = int(a[l]) + int(b[l]) + j
            # 判断进位
            if temp == 0 or temp == 1:
                res = str(temp) + res
                j = 0
            elif temp == 2:
                res = '0' + res
                j = 1
            else:
                res = '1' + res
                j = 1
            l -= 1
        if j == 1:
            res = '1' + res
        return res
