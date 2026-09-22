class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        nums.sort()
        diff = float("inf")

        # Slide a window of size k across the sorted array
        for i in range(len(nums) - k + 1):
            diff = min(diff, nums[i + k - 1] - nums[i])

        return int(diff)
        




        