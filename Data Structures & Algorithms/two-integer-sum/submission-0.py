class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sub = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in sub):
                return [sub.get(diff), i]
            sub[nums[i]] = i
            

        