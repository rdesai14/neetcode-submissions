class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        
        levels = 0
        while n > 0:
            levels += 1
            n -= levels
        
        if n < 0:
            return levels - 1
        else:
            return levels
        
        

        