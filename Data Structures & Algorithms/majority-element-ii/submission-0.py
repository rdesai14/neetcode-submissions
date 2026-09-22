class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        maj = len(nums) // 3

        for ele, val in map.items():
            if val > maj:
                res.append(ele)
        return res