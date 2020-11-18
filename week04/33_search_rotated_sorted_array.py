class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        # use <= because we want to search all candidates
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[high]:
                # array is increasing at right side, pivot point is at left side
                if nums[mid] < target <= nums[high]:
                    # if target value falls between nums[mid] and nums[high],
                    # then it must be between (mid, high], otherwise it's not found
                    low = mid + 1
                else:
                    # otherwise, the target value might be at the left side
                    high = mid - 1
            else:
                # array wraps around at right side, pivot point is at the right
                if nums[mid] < target or target <= nums[high]:
                    # target value will be right side, otherwise it's not found
                    low = mid + 1
                else:
                    # otherwise, search the left side
                    high = mid - 1
        return -1