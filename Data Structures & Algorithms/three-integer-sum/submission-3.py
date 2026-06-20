class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)

        triplets = set()

        for i in range(0, len(s_nums)):
            if s_nums[i] <= 0:
                j = i + 1
                k = len(s_nums) - 1
                while j < k:
                    trisum = s_nums[i] + s_nums[j] + s_nums[k]
                    if trisum == 0:
                        triplets.add((s_nums[i], s_nums[j], s_nums[k]))
                        j += 1
                    elif trisum < 0:
                        j += 1
                    else:
                        k -= 1
        
        return list(triplets)
                        
        