class Solution1:
    def originalDigits(self, s: str) -> str:
        # 判断0, 'z'
        i_0 = 0
        if 'z' in s:
            for i in s:
                if i == 'z':
                    i_0 += 1
            s = s.replace('z', '', i_0)
            s = s.replace('e', '', i_0)
            s = s.replace('r', '', i_0)
            s = s.replace('o', '', i_0)
        # 判断8, 'g'
        i_8 = 0
        if 'g' in s:
            for i in s:
                if i == 'g':
                    i_8 += 1
            s = s.replace('e', '', i_8)
            s = s.replace('i', '', i_8)
            s = s.replace('g', '', i_8)
            s = s.replace('h', '', i_8)
            s = s.replace('t', '', i_8)
        # 判断6, 'x'
        i_6 = 0
        if 'x' in s:
            for i in s:
                if i == 'x':
                    i_6 += 1
            s = s.replace('s', '', i_6)
            s = s.replace('i', '', i_6)
            s = s.replace('x', '', i_6)
        # 判断2, 'w'
        i_2 = 0
        if 'w' in s:
            for i in s:
                if i == 'w':
                    i_2 += 1
            s = s.replace('t', '', i_2)
            s = s.replace('w', '', i_2)
            s = s.replace('o', '', i_2)
        # 判断4, 'u'
        i_4 = 0
        if 'u' in s:
            for i in s:
                if i == 'u':
                    i_4 += 1
            s = s.replace('f', '', i_4)
            s = s.replace('o', '', i_4)
            s = s.replace('u', '', i_4)
            s = s.replace('r', '', i_4)
        # 判断1, 'o'
        i_1 = 0
        if 'o' in s:
            for i in s:
                if i == 'o':
                    i_1 += 1
            s = s.replace('o', '', i_1)
            s = s.replace('n', '', i_1)
            s = s.replace('e', '', i_1)
        # 判断5, 'f'
        i_5 = 0
        if 'f' in s:
            for i in s:
                if i == 'f':
                    i_5 += 1
            s = s.replace('f', '', i_5)
            s = s.replace('i', '', i_5)
            s = s.replace('v', '', i_5)
            s = s.replace('e', '', i_5)
        # 判断9, 'i'
        i_9 = 0
        if 'i' in s:
            for i in s:
                if i == 'i':
                    i_9 += 1
            s = s.replace('n', '', i_9 * 2)
            s = s.replace('i', '', i_9)
            s = s.replace('e', '', i_9)
        # 判断3, 't'
        i_3 = 0
        if 't' in s:
            for i in s:
                if i == 't':
                    i_3 += 1
            s = s.replace('t', '', i_3)
            s = s.replace('h', '', i_3)
            s = s.replace('r', '', i_3)
            s = s.replace('e', '', i_3 * 2)
        # 判断7, 's'
        i_7 = 0
        if 's' in s:
            for i in s:
                if i == 's':
                    i_7 += 1
        res = ''
        while i_0:
            res = res + '0'
            i_0 -= 1
        while i_1:
            res = res + '1'
            i_1 -= 1
        while i_2:
            res = res + '2'
            i_2 -= 1
        while i_3:
            res = res + '3'
            i_3 -= 1
        while i_4:
            res = res + '4'
            i_4 -= 1
        while i_5:
            res = res + '5'
            i_5 -= 1
        while i_6:
            res = res + '6'
            i_6 -= 1
        while i_7:
            res = res + '7'
            i_7 -= 1
        while i_8:
            res = res + '8'
            i_8 -= 1
        while i_9:
            res = res + '9'
            i_9 -= 1
        return res

class Solution2:
    def originalDigits(self, s: str) -> str:
        d = {}
        alpha = 'hzerontfuixvgws'
        for a in alpha:
            d[a] = 0
        for i in s:
            d[i] += 1
        res = [0,0,0,0,0,0,0,0,0,0]
        res[0] = d['z']
        res[2] = d['w']
        res[4] = d['u']
        res[6] = d['x']
        res[8] = d['g']
        res[1] = d['o'] - res[0] - res[2] - res[4]
        res[5] = d['f'] - res[4]
        res[9] = d['i'] - res[5] - res[6] - res[8]
        res[3] = d['t'] - res[2] - res[3] - res[8]
        res[7] = d['v'] - res[5]
        result = ''
        for i in range(len(res)):
            while res[i] > 0:
                result = result + str(i)
                res[i] -= 1
        return result


if __name__ == '__main__':
    s = Solution1()
    print(s.originalDigits("owoztneoer"))
