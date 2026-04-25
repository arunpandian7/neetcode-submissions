class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        amalgram = True

        for c1 in s:
            if s.count(c1) != t.count(c1):
                amalgram = False
        
        return amalgram
            

        