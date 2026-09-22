class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        for l in s:
            map[l] = map.get(l, 0) + 1
        
        for l in t:
            map[l] = map.get(l, 0) - 1
        
        for l, val in map.items():
            if val != 0:
                return False
        return True
        
        