class Solution:

    def is_equal_freq(self, a: str, b: str):
        mask = [0] * 26
        for a_c, b_c in zip(a, b):
            mask[ord(a_c) - ord('a')] += 1
            mask[ord(b_c) - ord('a')] -= 1
        return all(i == 0 for i in mask)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_len = len(s1)
        i = 0

        while (i + s1_len) <= len(s2):
            s2_sub = s2[i: i+s1_len]
            print(s2_sub)
            if self.is_equal_freq(s1, s2_sub):
                return True
            else:
                i +=1
        
        return False
            



            
        