class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for item in nums:
            if item not in dup:
                dup[item] = 1
            else:
                return True
        
        return False