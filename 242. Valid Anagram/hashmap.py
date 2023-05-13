class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_countS, char_countT = {}, {}

        for i in range(len(s)):
            char_countS[s[i]] = 1 + char_countS.get(s[i], 0)
            char_countT[t[i]] = 1 + char_countT.get(t[i], 0)
        for c in char_countS:
            if char_countS[c] != char_countT.get(c, 0):
                return False
            
        return True

