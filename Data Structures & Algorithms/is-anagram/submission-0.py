class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        s1 = {}
        s2 = {}

        for let in s:
            s1[let] = s1.get(let, 0) + 1
        
        for let in t:
            s2[let] = s2.get(let, 0) + 1
        
        for let in s:
            if (s1.get(let) != s2.get(let)):
                return False
        return True

        
        