class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix_prod = 1
        suffix_prod = 1
        for i in range(1, n):
            prefix_prod *= nums[i-1]
            suffix_prod *= nums[n - i]
            result[i] *= prefix_prod
            result[n - 1 - i] *= suffix_prod        
        
        return result
