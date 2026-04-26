class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_index = {}
        for i, n in enumerate(nums):
            j = search_index.get(target - n)
            if j is not None:
                return [j, i]
            search_index[n] = i

        