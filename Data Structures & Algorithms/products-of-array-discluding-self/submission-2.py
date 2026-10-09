class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0

        for i in nums:
            if i==0:
                zero_count += 1
            else:
                prod *= i
        
        result = []
        for i in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                result.append(prod if i==0 else 0)
            else:
                result.append(prod // i)
            
        return result

