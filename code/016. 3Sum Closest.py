"""
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。


例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        这里和3Sum类似,但是重点是：
        1.首先判断是否比之前的距离小
        2.第二次判断的是三个数之和和target的差别,这里就不需要和前者的距离进行比较了
        """
        n = len(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[n-1]
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == target:
                    return val
                if abs(val - target) < abs(target - ans):
                    ans = val
                if val < target:
                    left += 1
                else:
                    right -= 1
        return ans

if __name__ == '__main__':
    s = Solution()
    s.threeSumClosest([-1,2,1,-4], 1)