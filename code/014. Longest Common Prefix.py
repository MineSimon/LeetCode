class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        end, minl = 0, min([len(s) for s in strs])
        while end < minl:
            for i in strs:
                if strs[0][end] != i[end]:
                    return strs[0][:end]  # 通过直接返回可以不用考虑break两次，很聪明的做法
            end += 1
        return strs[0][:end]


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))