class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod, suf_prod = [1], [1]
        prefix_prod = 1
        suffix_prod = 1
        n = len(nums)
        for i in range(1, n):
            prefix_prod *= nums[i-1]
            pre_prod.append(prefix_prod)

        for i in range(n-2, -1, -1):
            suffix_prod *= nums[i+1]
            suf_prod.append(suffix_prod)

        result = []
        for i in range(n):
            prod = pre_prod[i] * suf_prod[n - 1 - i]
            result.append(prod)
        
        return result
