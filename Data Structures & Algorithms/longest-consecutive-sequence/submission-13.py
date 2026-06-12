class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        longest_len = 0
        for n in nums:
            if (n - 1) not in snums:
                length = 1
                while n + length in snums:
                    length += 1
                longest_len = max(longest_len, length)
        
        return longest_len
        