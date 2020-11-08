class Solution:
    def backtrack(self, nums: List[int], path: List[int], res: List[List[int]]):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], res)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        self.backtrack(nums, [], res)
        return res