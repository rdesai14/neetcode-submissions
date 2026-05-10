class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zct = 0
        for num in nums:
            if num == 0:
                zct+= 1
            else:
                prod *= num
        
        if zct > 1:
            return [0] * len(nums)
        
        res = []
        for num in nums:
            if zct == 1:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(int(prod // num))
        return res
        

        