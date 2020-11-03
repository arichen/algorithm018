class Solution:
    def genUgly(self, n: int = 1690) -> int:
        nums = [1]
        p2 = p3 = p5 = 0

        for i in range(1, n):
            v = min(nums[p2] * 2, nums[p3] * 3, nums[p5] * 5)
            nums.append(v)

            if v == nums[p2] * 2:
                p2 += 1
            if v == nums[p3] * 3:
                p3 += 1
            if v == nums[p5] * 5:
                p5 += 1
        return nums

    def nthUglyNumber(self, n: int) -> int:
        nums = self.genUgly(n)
        return nums[-1]