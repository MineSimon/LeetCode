class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_sum = nums[0]
        sum_ = 0
        for num in nums:
            sum_ += num
            if sum_ > max_sub_sum:
                max_sub_sum = sum_
            if sum_ < 0:
                sum_ = 0
        return max_sub_sum
