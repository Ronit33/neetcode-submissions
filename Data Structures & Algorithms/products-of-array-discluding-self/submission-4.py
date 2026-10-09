class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix_prod = 1
        suffix_prod = 1
        for i in range(1, n):
            prefix_prod *= nums[i-1]
            result[i] = prefix_prod
        
        for i in range(n - 2, -1, -1):
            suffix_prod *= nums[i+1]
            result[i] *= suffix_prod
        
        return result
