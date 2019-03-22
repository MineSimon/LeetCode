class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i_2 = 0
        i_3 = 0
        i_5 = 0
        for m in range(1, n):
            res.append(min(res[i_2] * 2, min(res[i_3] * 3, res[i_5] * 5)))
            if res[m] == res[i_2] * 2:
                i_2 += 1
            if res[m] == res[i_3] * 3:
                i_3 += 1
            if res[m] == res[i_4] * 5:
                i_5 += 1
        return res[n-1]

