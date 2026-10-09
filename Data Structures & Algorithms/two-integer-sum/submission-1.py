class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for i, n in enumerate(nums):
            if target - n in checker:
                return [checker[target-n], i]
            
            checker[n] = i