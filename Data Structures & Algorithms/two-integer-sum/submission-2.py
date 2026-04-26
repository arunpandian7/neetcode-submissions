class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_index = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in search_index:
                return [search_index[complement], i]
            search_index[n] = i

        