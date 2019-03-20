class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        result = []
        candidates.sort()
        self._combinationSum(candidates, target, 0, list(), result)
        return result

    def _combinationSum(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return

        if path and target < path[-1]:
            # 回溯
            path.pop()
            return

        for i in range(index, len(nums)):
            self._combinationSum(nums, target - nums[i], i, path + [nums[i]], res)


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
