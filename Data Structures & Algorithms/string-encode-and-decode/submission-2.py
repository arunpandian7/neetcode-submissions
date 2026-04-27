class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            length = len(s)
            encoded_str += f"{length}#{s}"
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded_list = []
        i = 1
        prev_c = s[i-1]
        while i < len(s):
            curr_c = s[i]
            if curr_c == "#":
                length = int(prev_c)
                decoded_list.append(s[i+1:i+length+1])
                prev_c = ""
                i += max(1, length+1)
            else:
                prev_c += curr_c
                i += 1
        return decoded_list
