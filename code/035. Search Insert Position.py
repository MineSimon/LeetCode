class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)-1):
                if target > nums[i] and target <= nums[i+1]:
                    return i+1


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        # 如果前面没返回, 说明数字不存在且应该插入在最右端, 则应返回len(nums), 即i+1
        return i+1
