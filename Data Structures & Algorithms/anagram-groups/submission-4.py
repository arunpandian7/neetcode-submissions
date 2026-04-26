class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_sign_grps = defaultdict(list) 
        get_char_index = lambda x: ord(x.lower()) - ord('a')
        for string in strs:
            string_mask = [0] * 26
            for char in string:
                string_mask[get_char_index(char)] += 1
            string_sign_grps[tuple(string_mask)].append(string)
        return list(string_sign_grps.values())

        