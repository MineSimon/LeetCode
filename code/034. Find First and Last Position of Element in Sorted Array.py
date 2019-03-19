"""
34. 在排序数组中查找元素的第一个和最后一个位置(Find First and Last Position of Element in Sorted Array)

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

"""



class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            if nums[left] < target:
                left += 1
            if nums[right] > target:
                right -= 1
            # 这里需要一个判断，当系统找到两个相同的数字时，会一直循环不会跳出
            if left <= right and nums[left] == nums[right] == target:
                return[left, right]
        # 若while循环跳出，则说明找不到响应的数字，则返回[-1, -1]
        return[-1, -1]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 6))