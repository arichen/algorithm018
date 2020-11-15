class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # mark the point from where can get to the end
        length = len(nums)
        mark = length - 1
        for i in range(length - 2, -1, -1):
            if i + nums[i] >= mark:
                mark = i
        return mark == 0
