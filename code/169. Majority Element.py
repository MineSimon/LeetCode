class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count, n = 0, 0
        for num in nums:
            if count == 0:
                n = num
            if num != n:
                count -= 1
            else:
                count += 1
        return n