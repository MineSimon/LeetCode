class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(l1-l2+1):
            if haystack[i] == needle[0]:
                for j in range(1, l2):
                    if haystack[i+j] != needle[j]:
                        break
                else:
                    return i
        return -1
