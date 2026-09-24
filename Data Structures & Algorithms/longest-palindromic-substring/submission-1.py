class Solution:
    def longestPalindrome(self, s: str) -> str:

        
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1 : r]

        res = ""

        for i in range(0, len(s)):

            even = helper(s, i, i +1)
            odd = helper(s, i, i)

            res = max(odd, even, res, key=len)

        return res





        