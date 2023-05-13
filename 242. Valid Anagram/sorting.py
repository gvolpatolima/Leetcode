class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_Schars = sorted(list(s))
        sorted_s = ''.join(sorted_Schars)

        sorted_Tchars = sorted(list(t))
        sorted_t = ''.join(sorted_Tchars)
    
        if sorted_t == sorted_s:
            return True
        else:
            return False