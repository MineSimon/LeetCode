class Solution:
    def permute(self, nums: list) -> list:
        self.res = []
        self.max_len = len(nums)
        self._permute([], nums)
        return self.res

    def _permute(self, l, r):
        if r == []:
            self.res.append(l)
            return

        for i, num in enumerate(r):
            # l += [num]
            self._permute(l+[num], r[:i] + r[i + 1:])


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
