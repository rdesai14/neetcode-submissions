class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (not nums):
            return 0
        heap = nums[:]
        heapq.heapify(heap)
        res = 1
        curr = 1
        lastval = float('-inf')
        while heap:
            removed = heapq.heappop(heap)
            if removed == lastval:
                continue
            if (removed - lastval) == 1:
                curr += 1
                res = max(res, curr)
            else:
                curr = 1
            lastval = removed
        return res
        