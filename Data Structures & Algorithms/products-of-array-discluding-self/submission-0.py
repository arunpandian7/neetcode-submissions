import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prefix_prod = math.prod(nums[:i])
            suffix_prod = math.prod(nums[i+1:])
            result.append(prefix_prod * suffix_prod)
        return result
            
        