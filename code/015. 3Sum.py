class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        这个代码我一直都是超时的,也不知道为什么
        后来才发现,当我判断三个数是否重复的时候,时间就必然会超时
        这里我们直接通过排除相同的数字,来直接去除重复的可能性(这一点很重要)
        这样的话就可以减少确认重复的时间
        
        还有很多小细节可以减少时间,这个算法的重点就是去除重复工作
        """
        ans = []
        n = len(nums)
        if n < 3:
            return ans
        # 通过排序来更好的选择数组
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0:
                break
            # 第一次和前两个数相同时, 直接跳过, 减少重复
            if i == 0 or nums[i] > nums[i-1]:
                left = i + 1
                right = n - 1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum == 0: # and [nums[i], nums[left], nums[right]] not in ans:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # 跳过重复数字
                        while left < right and nums[left]==nums[left-1]:
                            left += 1
                        # 跳过重复数字
                        while left < right and nums[right]==nums[right+1]:
                            right -=1
                    elif sum < 0:
                        # 跳过重复数字
                        while left < right:
                            left += 1
                            if nums[left] > nums[left-1]:
                                break
                    else:
                        # 跳过重复数字
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right+1]:
                                break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))