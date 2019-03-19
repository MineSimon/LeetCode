class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        使用两个指针, 使偏小的数字向另一个指针移动
        这样时间复杂度为len(height)
        相比暴力求解降低了一个次方的复杂度
        """
        lp, rp = 0, len(height)-1
        max_a = (rp-lp)*min(height[lp], height[rp])
        while lp < rp:
            if height[lp]<height[rp]:
                lp += 1
            else:
                rp -= 1
            max_a = max(max_a, (rp-lp)*min(height[lp], height[rp]))
        return max_a


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
