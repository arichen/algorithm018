class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count, n = 0, len(nums)
        k %= n

        start = 0
        while count < n:
            current = start
            while True:
                next_idx = (current + k) % n
                nums[start], nums[next_idx] = nums[next_idx], nums[start]
                current = next_idx
                count += 1

                if current == start:
                    break
            start += 1