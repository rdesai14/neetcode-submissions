class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lptr = 0
        rptr = len(heights) - 1
        res = 0

        area = 1

        while (lptr < rptr):

            area = min(heights[lptr], heights[rptr]) * (rptr - lptr)
            res = max(res, area)

            if (heights[lptr] <= heights[rptr]):
                lptr += 1
            else: 
                rptr -= 1
        return res
            
            

            