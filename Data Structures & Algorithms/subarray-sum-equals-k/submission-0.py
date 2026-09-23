class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0 : 1}

        prefixSum = 0

        res = 0

        for num in nums:
            prefixSum += num

            rem = prefixSum - k

            res += mp.get(rem, 0)
            mp[prefixSum] = mp.get(prefixSum, 0) + 1
        
        return res







        