class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * (len(nums))
        l = 0
        r = len(nums) - 1

        product = 1
        while l < len(nums):
            out[l] = product
            product *= nums[l]
            l += 1

        product = 1
        while r >= 0:
            out[r] *= product
            product *= nums[r]        

            r -= 1
        return out
        