"""
解法1：
1.从左向右找到不符合升序的最大下标, 即判断当前的下标是否是从左到右的最大值,
  若不是, 则说明当前下标左边存在更大的数, 需要进行排序
2.从右往左找到不符合降序的最小下标, 与1同理
3.返回值

"""
class Solution1:
    def findUnsortedSubarray(self, nums: list) -> int:
        if len(nums) <= 1:
            return 0

        left = 0
        right = len(nums) - 1

        l = len(nums) - 1
        mmax = nums[0]
        mmin = nums[-1]

        for i in range(len(nums)):

            if left > right:
                mmax = max(mmax, nums[i])
                if nums[i] != mmax:
                    left = i

                mmin = min(mmin, nums[l - i])
                if nums[l - i] != mmin:
                    right = l - i
            else:
                return 0

        return left - right + 1 if left > right else 0

"""
解法2:
1.将nums进行拷贝并排序
2.对比两者之间相同部分
3.返回不同的部分即最小排序长度
"""
class Solution2():
    def findUnsortedSubarray(self, nums: list) -> int:
        left = 0
        right = len(nums) - 1
        l = len(nums)-1
        s = sorted(nums)
        while left < l and nums[left] == s[left]:
            left += 1
        while right > 0 and nums[right] == s[right]:
            right -= 1
        return right - left + 1 if right>left else 0



if __name__ == '__main__':
    s = Solution2()
    print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
