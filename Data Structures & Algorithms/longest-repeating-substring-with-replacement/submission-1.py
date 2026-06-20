class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_set = set([c for c in s])

        for c in char_set:
            l, r = 0, 0
            count = 0
            while r < len(s):
                window_size = (r - l) + 1
                if s[r] == c:
                    count += 1
                
                if (window_size - count) > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                    continue
                
                else:
                    res = max(res, window_size)
                    r += 1

        return res


                


        