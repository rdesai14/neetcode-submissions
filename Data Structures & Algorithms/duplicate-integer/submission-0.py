class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dup = {}

        for num in nums:
            dup[num] = dup.get(num, 0) + 1
            if (dup.get(num) > 1):
                return True

        return False
        