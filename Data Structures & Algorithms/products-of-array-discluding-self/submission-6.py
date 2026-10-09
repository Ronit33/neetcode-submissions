class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix_prod = 1
        suffix_prod = 1
        for i in range(n):
            j = n - 1 - i

            result[i] *= prefix_prod
            prefix_prod *= nums[i]

            result[j] *= suffix_prod
            suffix_prod *= nums[j]

        return result
