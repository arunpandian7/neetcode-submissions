class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_len = 0

        for i, n in enumerate(nums):
            j = 0
            if (n-1) not in nums_set:
                while n + j in nums_set:
                    j += 1
                longest_len = max(longest_len, j)
        
        return longest_len
                

        