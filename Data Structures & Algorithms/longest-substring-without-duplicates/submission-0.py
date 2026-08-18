class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        charSet = set() #ONLY Contain one of each

        l, r = 0, len(s) - 1 

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res,r-l+1)

        return res