class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        fix = 0
        while fix < len(nums) - 2:
            if fix > 0 and nums[fix] == nums[fix - 1]:
                fix += 1
                continue

            lptr = fix + 1
            rptr = len(nums) - 1

            while lptr < rptr:
                total = nums[fix] + nums[lptr] + nums[rptr]

                if total < 0:
                    lptr += 1
                elif total > 0:
                    rptr -= 1
                else:
                    out.append([nums[fix], nums[lptr], nums[rptr]])
                    lptr += 1
                    rptr -= 1

                    while lptr < rptr and nums[lptr] == nums[lptr - 1]:
                        lptr += 1
                    while lptr < rptr and nums[rptr] == nums[rptr + 1]:
                        rptr -= 1

            fix += 1
        return out