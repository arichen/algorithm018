class Solution:
    def jump(self, nums: List[int]) -> int:
        # algorithm: bfs search for shortest path to the end
        # 1. start with first element, find the farthest location we can reach from it, which is nums[0].
        # 2. the range we can reach for the next jump would then be (1, nums[0]],
        #    scan through the elements and find the farthest reachable location in next jump.
        # 3. repeat for the next jump

        steps = 0
        start, end, n = 0, 0, len(nums)

        # when end reaches (n - 1), it reaches our destination
        while end < n - 1:
            steps += 1
            # increase step count by 1 at each loop

            next_end = end
            # next_end will be the new ending boundary for next level

            for i in range(start, end + 1):
                next_end = max(i + nums[i], next_end)
                # look for the farthest location that can be reached from this level

            start = end + 1
            end = next_end
        return steps