class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res = 0
        x_jud = x
        while True:
            pop = x %10
            x = x//10
            res = res * 10 + pop
            if x == 0:
                break
        if x_jud == res:
            return True
        else:
            return False


class Solution2:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """
        通过计算一半的大小, 就可以直接可以判断数字是否为回文数
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        res = 0
        while res < x:
            res = res * 10 + x % 10
            x = x // 10

        return x == res or res // 10 == x


if __name__ == '__main__':
    s1 = Solution()
    s2 = Solution2()
    print(s1.isPalindrome(121), s1.isPalindrome(120), s1.isPalindrome(12321))
    print(s2.isPalindrome(121), s2.isPalindrome(120), s2.isPalindrome(12321))